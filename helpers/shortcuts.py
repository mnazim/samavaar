from sqlalchemy.orm.exc import (NoResultFound,
                                MultipleResultsFound)
from sqlalchemy.exc import (StatementError)
from werkzeug.exceptions import abort

def get_object_or_404(model, *criterion):
    """
    Usage:
        thing = get_object_or_404(Thing, Thing.slug == slug)
    """
    try:
        return model.query.filter(*criterion).one()
    except NoResultFound, MultipleResultsFound:
        abort(404)
