from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from app.models import *

def equijoins(request):
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno='10')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2024)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__month=1,hiredate__day=21)

    EMPOBJECTS=Emp.objects.select_related('deptno').filter(ename='SMITH' ,deptno__dname='RESEARCH')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(ename__startswith='S')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=False)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=True)
    EMPOBJECTS=Emp.objects.select_related('deptno').all()[:4]
    EMPOBJECTS=Emp.objects.select_related('depto').filter(hiredate__year=2024)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__month=1,hiredate__day=23)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(sal__lte=1000)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=False)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(sal__gte=1000,sal__lte=3000)

    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoins.html',d)

def selfjoins(request):
    empmgrobject=Emp.objects.select_related('mgr').all()
    empmgrobject=Emp.objects.select_related('mgr').filter(mgr__ename='KING')
    empmgrobject=Emp.objects.select_related('mgr').filter(sal__gte=2500)
    empmgrobject=Emp.objects.select_related('mgr').filter(mgr__ename='KING')
    empmgrobject=Emp.objects.select_related('mgr').filter(ename='KING')
    empmgrobject=Emp.objects.select_related('mgr').filter(mgr__ename='SCOTT')
    empmgrobject=Emp.objects.select_related('mgr').filter(mgr__ename='KING',sal__gte=2500)
    empmgrobject=Emp.objects.select_related('mgr').filter(mgr__isnull=False)
    empmgrobject=Emp.objects.select_related('mgr').filter(mgr__isnull=True)
    empmgrobject=Emp.objects.select_related('mgr').filter(mgr__ename__startswith='k')
    empmgrobject=Emp.objects.select_related('mgr').filter(hiredate__year=2024)
    empmgrobject=Emp.objects.select_related('mgr').filter(hiredate__month=1,hiredate__day=23)
    empmgrobject=Emp.objects.select_related('mgr').filter(sal__lte=1000)
    empmgrobject=Emp.objects.select_related('mgr').filter(comm__isnull=False)
    empmgrobject=Emp.objects.select_related('mgr').filter(sal__gte=1000,sal__lte=3000)

    d={'empmgrobject':empmgrobject }
    return render(request,'selfjoins.html',d)


def emp_mgr_dept(request):
    emd=Emp.objects.select_related('deptno','mgr').all()
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='RESEARCH')
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='BLAKE')
    emd=Emp.objects.select_related('deptno','mgr').filter(ename='MARTIN')
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno=20,deptno__dname='RESEARCH')
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='KING')
    emd=Emp.objects.select_related('deptno','mgr').filter(sal__gte=2500)
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='SCOTT')
    emd=Emp.objects.select_related('deptno','mgr').filter(ename='KING')
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dlocation='BOSTON')

    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='KING',sal__gte=2500)
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__isnull=False)
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__isnull=True)
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename__startswith='k')
    emd=Emp.objects.select_related('deptno','mgr').filter(hiredate__year=2024)
    emd=Emp.objects.select_related('deptno','mgr').filter(hiredate__month=1,hiredate__day=23)
    emd=Emp.objects.select_related('deptno','mgr').filter(ename='KING',mgr__ename='SCOTT')
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno=20) | Q(sal__gte=2000))
    emd=Emp.objects.select_related('deptno','mgr').order_by('ename')
    emd=Emp.objects.select_related('deptno','mgr').filter(sal=3000)

    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename__startswith='K')
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dlocation='CHICAGO')
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='KING')
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='ACCOUNTING',deptno=10)
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dlocation='BOSTON')
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dlocation='CHICAGO',sal__gte=2500)
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno=20)| Q(deptno__dname='SALES'))
    emd=Emp.objects.select_related('deptno','mgr').filter(job='CLERK',deptno=20)
    emd=Emp.objects.select_related('deptno','mgr').filter(job='SALESMAN',deptno__dlocation='NEW YORK')
    emd=Emp.objects.select_related('deptno','mgr').filter(sal=5000,deptno__dname='SALES')

    emd=Emp.objects.select_related('deptno','mgr').filter(ename='SMITH')
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='BLAKE')
    emd=Emp.objects.select_related('deptno','mgr').filter(sal__gte=3000)
    emd=Emp.objects.select_related('deptno','mgr').order_by('job')
    emd=Emp.objects.select_related('deptno','mgr').order_by('deptno__dlocation')
    emd=Emp.objects.select_related('deptno','mgr').filter(ename='JONES')
    emd=Emp.objects.select_related('deptno','mgr').filter(ename='KING',deptno__dlocation='SALES')
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='SCOTT',deptno=20)
    emd=Emp.objects.select_related('deptno','mgr').filter(job='MANAGER',deptno__dname='ACCOUNTING')
    emd=Emp.objects.select_related('deptno','mgr').filter(job='PRESIDENT')

    d={'emd':emd}
    return render(request,'emp_mgr_dept.html',d)