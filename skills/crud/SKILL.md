---
name: crud
description: Repository and service layer patterns, pagination, and CRUD conventions for FastAPI resources. Load when building standard create/read/update/delete endpoints or resource management features.
allowed-tools: Read, Write, Edit, Bash
---

## Layered Pattern

```
Router (HTTP only)
  └── Service (business logic)
        └── Repository (DB queries)
              └── Model (SQLAlchemy)
```

### Repository
```python
class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, user_id: int) -> User | None:
        result = await self.session.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()

    async def create(self, data: dict) -> User:
        user = User(**data)
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user
```

### Pagination
- Standard: `skip=0`, `limit=20`, max `limit=100`
- Always return total count alongside results

## Known Gotchas

- **Async pitfall:** Never use `time.sleep()` in async code — use `await asyncio.sleep()`
- **Pydantic v2:** Use `model_validate()` not `parse_obj()`, `model_dump()` not `dict()`
- **Redis cache keys:** Follow pattern `{resource}:{id}:{version}` — do not invent new patterns
- **CORS:** `ALLOWED_ORIGINS` must be explicit in production — `*` is local dev only

## Checklist

- [ ] Repository handles all DB access — no direct model access in services
- [ ] Service owns all business logic — no logic in routers
- [ ] Pagination on all list endpoints
- [ ] `response_model` declared on all endpoints
- [ ] Custom exceptions used — no raw `HTTPException` in services
