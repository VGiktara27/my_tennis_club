from members.models import Member


def test_fun():
    member1 = Member(firstname="Firox", lastname="Ravi")
    member2 = Member(firstname="one", lastname="sharma")
    member3 = Member(firstname="Firox", lastname="sharma")
    member4 = Member(firstname="Fia", lastname="Ravi")
    member5 = Member(firstname="Fix", lastname="Ravi")

    member_list = [member1, member2, member3, member4, member5]

    for i in member_list:
        print(f"type =={type(i)}")
        print(f"value =={i}")
        i.save()
    #    entry in member_list
    print(f"Member.object.all().values() == {Member.objects.all().values()}")
    print(i.delete())
