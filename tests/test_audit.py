from audit.engine import audit_all_tools


def test_chatgpt_team_small_users():

    tools = {
        "chatgpt": {
            "plan": "team",
            "spend": 60,
            "users": 2
        },
        "copilot": {
            "plan": "individual",
            "spend": 10,
            "users": 1
        }
    }

    result = audit_all_tools(tools, "coding")

    assert result["total_savings"] == 20


def test_chatgpt_no_savings():

    tools = {
        "chatgpt": {
            "plan": "plus",
            "spend": 20,
            "users": 1
        },
        "copilot": {
            "plan": "individual",
            "spend": 10,
            "users": 1
        }
    }

    result = audit_all_tools(tools, "coding")

    assert result["total_savings"] == 0


def test_copilot_business_small_team():

    tools = {
        "chatgpt": {
            "plan": "plus",
            "spend": 20,
            "users": 1
        },
        "copilot": {
            "plan": "business",
            "spend": 38,
            "users": 2
        }
    }

    result = audit_all_tools(tools, "coding")

    assert result["total_savings"] == 18


def test_multiple_savings():

    tools = {
        "chatgpt": {
            "plan": "team",
            "spend": 60,
            "users": 2
        },
        "copilot": {
            "plan": "business",
            "spend": 38,
            "users": 2
        }
    }

    result = audit_all_tools(tools, "coding")

    assert result["total_savings"] == 38


def test_empty_tools():

    tools = {
        "chatgpt": {
            "plan": "",
            "spend": 0,
            "users": 0
        },
        "copilot": {
            "plan": "",
            "spend": 0,
            "users": 0
        }
    }

    result = audit_all_tools(tools, "coding")

    assert result["total_savings"] == 0