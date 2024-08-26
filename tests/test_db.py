from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(username="user", email="email@email.com", password="123")
    session.add(user)
    session.commit()
    result = session.scalar(
        select(User).where(User.email == "email@email.com")
    )
    session.refresh(user)

    assert result.username == "user"
