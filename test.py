
import pytest
import cpsc2120_lab3


@pytest.mark.parametrize("inputfilename, results", [
    ('sample.txt', """Group 1:  (0,9) (1,9)
Group 2:  (1,3) (1,4)
Group 3:  (3,4)
Group 4:  (3,7) (4,7) (5,7) (5,8)
Group 5:  (4,3)
Group 6:  (6,4) (6,5)"""),
    ('sample2.txt', "Group 1")
])
def test_example_output(inputfilename, results, capsys):
    cpsc2120_lab3.main(inputfilename)

    out, err = capsys.readouterr()

    assert results in out
    print(out)

def test_parse():
    field = [ ".X" ]
    nodes = cpsc2120_lab3.parse(field)
    assert len(nodes) == 2


def test_flood_group_at():
    field = ["XXX."]
    nodes = cpsc2120_lab3.parse(field)

    group = cpsc2120_lab3.flood_fill_recursive(0, 1, nodes)

    assert len(group) == 3
    assert group == [(0, 1), (0, 0), (0, 2)]


def test_render_node_field():
    field = ["X.", "XX", ".X"]
    nodes = cpsc2120_lab3.parse(field)

    rendered_field = cpsc2120_lab3.node_field(nodes)
    assert field == list(rendered_field)


def test_flood_group_follow_corners():
    field = ["X.", "XX", ".X"]
    nodes = cpsc2120_lab3.parse(field)

    group = cpsc2120_lab3.flood_fill_recursive(0, 0, nodes)

    assert len(group) == 4
    assert group == [(0, 0), (1, 0), (1, 1), (2, 1)]

def test_flood_group_follow_deq():
    field = ["X.", "XX", ".X"]
    nodes = cpsc2120_lab3.parse(field)

    group = cpsc2120_lab3.flood_fill_deque(0, 0, nodes)

    assert len(group) == 4
    assert group == [(0, 0), (1, 0), (1, 1), (2, 1)]

    print("Resulting field")
    print("\n".join(cpsc2120_lab3.node_field(nodes)))

def test_flood_group_deque_center():
    # Worst-case memory pressure.
    field = ["XXX", "XXX", "XXX"]
    nodes = cpsc2120_lab3.parse(field)

    group = cpsc2120_lab3.flood_fill_deque(1, 1, nodes)

    assert len(group) == 9

    print("Resulting field")
    print("\n".join(cpsc2120_lab3.node_field(nodes)))