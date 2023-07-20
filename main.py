from admin_portal import Admin_Portal
from member_portal import Member_Portal


if __name__ == "__main__":
    member_name = input("Enter member name: ")

    # normal member
    if member_name != 'admin':
        portal = Member_Portal(member_name)
        portal.execute()
    else:
        portal = Admin_Portal()
        portal.execute()