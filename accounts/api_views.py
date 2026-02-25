from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from tracker.models import Skill
from tracker.models import Skill, StudyTask


@api_view(['GET'])
def skills_api(request):
    if not request.user.is_authenticated:
        return Response({"error": "Unauthorized"}, status=401)

    skills = Skill.objects.filter(user=request.user)

    data = []
    for skill in skills:
        data.append({
            "name": skill.name,
            "hours_spent": skill.hours_spent
        })

    return Response(data)



@api_view(['GET'])
def tasks_api(request):
    if not request.user.is_authenticated:
        return Response({"error": "Unauthorized"}, status=401)

    tasks = StudyTask.objects.filter(user=request.user)

    data = []
    for task in tasks:
        data.append({
            "title": task.title,
            "is_completed": task.is_completed
        })

    return Response(data)



@api_view(['GET'])
def progress_api(request):
    if not request.user.is_authenticated:
        return Response({"error": "Unauthorized"}, status=401)

    tasks = StudyTask.objects.filter(user=request.user)

    total_tasks = tasks.count()
    completed_tasks = tasks.filter(is_completed=True).count()

    completion_percentage = 0
    if total_tasks > 0:
        completion_percentage = int((completed_tasks / total_tasks) * 100)

    return Response({
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "completion_percentage": completion_percentage
    })