from flask import Blueprint


bp = Blueprint('filters', __name__)


@bp.app_template_filter()
def length(value) -> int:
    return len(value)
