from handlers.ping import router as ping_router
from handlers.tasks import router as task_router
from handlers.categories import router as category_router
from handlers.users import router as user_router
from handlers.auth import router as auth_router

routers = [ping_router, task_router, category_router, user_router, auth_router]
