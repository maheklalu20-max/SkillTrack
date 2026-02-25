from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from tracker.models import Skill, Note
from datetime import date, datetime
import json
from tracker.models import StudyTask
from django.utils import timezone

# ==========================
# REGISTER
# ==========================
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        return redirect("login")

    return render(request, "accounts/register.html")


# ==========================
# LOGIN
# ==========================
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid credentials")

    return render(request, "accounts/login.html")


# ==========================
# LOGOUT
# ==========================
def user_logout(request):
    logout(request)
    return redirect("login")


# ==========================
# DELETE SKILL
# ==========================
@login_required
def delete_skill(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id, user=request.user)
    skill.delete()
    return redirect("dashboard")


# ==========================
# DASHBOARD
# ==========================
@login_required
def dashboard(request):

    # -------- HANDLE POST --------
    if request.method == "POST":
        name = request.POST.get("name")
        hours = request.POST.get("hours")
        note_content = request.POST.get("note")

        if name and hours:
            skill, created = Skill.objects.get_or_create(
                user=request.user,
                name=name
            )

            if not created:
                skill.hours_spent += int(hours)
            else:
                skill.hours_spent = int(hours)

            skill.save()

            # Create note if provided
            if note_content:
                Note.objects.create(
                    user=request.user,
                    skill=skill,
                    content=note_content
                )

            request.session["last_active"] = str(date.today())
            return redirect("dashboard")

    # -------- FETCH DATA --------
    skills = Skill.objects.filter(user=request.user)

    # Skill Level Logic
    for skill in skills:
        if skill.hours_spent <= 10:
            skill.level = "Beginner 🌱"
        elif skill.hours_spent <= 30:
            skill.level = "Intermediate ⚡"
        elif skill.hours_spent <= 60:
            skill.level = "Advanced 🚀"
        else:
            skill.level = "Expert 🏆"

    total_hours = sum(skill.hours_spent for skill in skills)

    # -------- STREAK LOGIC --------
    today = date.today()
    last_active = request.session.get("last_active")
    streak = request.session.get("streak", 1)

    if last_active:
        last_date = datetime.strptime(last_active, "%Y-%m-%d").date()

        if last_date == today:
            pass
        elif (today - last_date).days == 1:
            streak += 1
        else:
            streak = 1

    request.session["streak"] = streak

    # -------- ANALYTICS FOR CHARTS --------
    skill_names = json.dumps([skill.name for skill in skills])
    skill_hours = json.dumps([skill.hours_spent for skill in skills])

    return render(request, "accounts/dashboard.html", {
        "skills": skills,
        "total_hours": total_hours,
        "streak": streak,
        "skill_names": skill_names,
        "skill_hours": skill_hours,
    })


# ==========================
# PROFILE
# ==========================
@login_required
def profile(request):
    skills = Skill.objects.filter(user=request.user)
    total_hours = sum(skill.hours_spent for skill in skills)
    total_skills = skills.count()

    milestone = 100
    progress_percentage = min((total_hours / milestone) * 100, 100)

    return render(request, "accounts/profile.html", {
        "total_hours": total_hours,
        "total_skills": total_skills,
        "progress_percentage": progress_percentage,
    })
# ==========================
# study planner
# ==========================
@login_required
def study_planner(request):

    if request.method == "POST":
        task_title = request.POST.get("task")

        if task_title:
            StudyTask.objects.create(
                user=request.user,
                title=task_title
            )
            return redirect("study_planner")

    # Show ALL tasks for now (no date filter)
    tasks = StudyTask.objects.filter(user=request.user)

    total_tasks = tasks.count()
    completed_tasks = tasks.filter(is_completed=True).count()

    completion_percentage = 0
    if total_tasks > 0:
        completion_percentage = int((completed_tasks / total_tasks) * 100)

    return render(request, "accounts/study_planner.html", {
        "tasks": tasks,
        "completion_percentage": completion_percentage,
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
    })
# ==========================
# toggle task
# ==========================

@login_required
def toggle_task(request, task_id):
    task = StudyTask.objects.get(id=task_id, user=request.user)
    task.is_completed = not task.is_completed
    task.save()
    return redirect("study_planner")
# ==========================
# to delete task
# ==========================
@login_required
def delete_task(request, task_id):
    task = StudyTask.objects.get(id=task_id, user=request.user)
    task.delete()
    return redirect("study_planner")