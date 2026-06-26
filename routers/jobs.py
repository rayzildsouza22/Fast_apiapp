from fastapi import APIRouter

router=APIRouter(prefix="/jobs", tags=["jobs"])

@router.get("/")
def read_jobs():
    return {"jobs": "Jobs root."}

@router.get("/{job_id}")
def read_job(job_id: int):
    return {"job_id": job_id}   
