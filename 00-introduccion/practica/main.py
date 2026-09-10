from fastapi import Body, FastAPI, HTTPException, Query, status

app = FastAPI(title="Arsenal for cybersecurity")
TOOLS = [
    {
        "id": 1,
        "name": "theHarvester",
        "category": "Reconnaissance",
        "difficulty": "Beginner",
        "description": "Open-source intelligence gathering tool used to harvest emails, subdomains, hosts, and employee names from public sources.",
    },
    {
        "id": 2,
        "name": "Nmap",
        "category": "Scanning",
        "difficulty": "Beginner",
        "description": "Network discovery and vulnerability scanning tool used to discover active hosts, open ports, and running services.",
    },
    {
        "id": 3,
        "name": "Burp Suite",
        "category": "Scanning",
        "difficulty": "Intermediate",
        "description": "Web vulnerability scanner and intercepting proxy used to analyze and test application-layer security.",
    },
    {
        "id": 4,
        "name": "Metasploit",
        "category": "Exploitation",
        "difficulty": "Intermediate",
        "description": "Comprehensive penetration testing framework used to verify, develop, and execute exploit payloads against target machines.",
    },
    {
        "id": 5,
        "name": "SQLmap",
        "category": "Exploitation",
        "difficulty": "Intermediate",
        "description": "Automated open-source tool designed to detect and exploit SQL injection flaws and take control of database servers.",
    },
    {
        "id": 6,
        "name": "John the Ripper",
        "category": "Post-Exploitation",
        "difficulty": "Intermediate",
        "description": "Fast password cracking utility used to audit offline password hashes obtained from compromised systems.",
    },
    {
        "id": 7,
        "name": "Mimikatz",
        "category": "Post-Exploitation",
        "difficulty": "Advanced",
        "description": "Post-exploitation tool capable of extracting plaintext passwords, hashes, PIN codes, and Kerberos tickets from Windows memory.",
    },
    {
        "id": 8,
        "name": "Wireshark",
        "category": "Defense",
        "difficulty": "Intermediate",
        "description": "Packet analyzer used by defenders to capture and inspect live network traffic to detect anomalies and intrusions.",
    },
]


# Welcome endpoint
@app.get("/")
def welcome():
    return {
        "message": 'Welcome to "Arsenal for Cybersecurity"',
        "author": "Francisco Nieto",
        "version": "1.0.0",
    }


# List of tools
@app.get("/tools")
def list_tools(
    query: str | None = Query(default=None, description="Text to filter tool"),
    category: str | None = Query(
        default=None, description="Text to filter the tool by category"
    ),
    difficulty: str | None = Query(
        default=None, description="Text to filter the tool by difficulty"
    ),
    include_description: bool = Query(
        default=False, description="Include description field"
    ),
):
    filtered = TOOLS

    if query:
        filtered = [tool for tool in filtered if query.lower() in tool["name"].lower()]

    if category:
        filtered = [
            tool for tool in filtered if category.lower() in tool["category"].lower()
        ]

    if difficulty:
        filtered = [
            tool
            for tool in filtered
            if difficulty.lower() in tool["difficulty"].lower()
        ]

    results = []

    for tool in filtered:
        item = {
            "id": tool["id"],
            "name": tool["name"],
            "category": tool["category"],
            "difficulty": tool["difficulty"],
        }
        if include_description:
            item["description"] = tool["description"]

        results.append(item)

    return {"data": results}


@app.get("/tools/{tool_id}")
def get_tool(
    tool_id: int, include_description: bool = Query(default=False, description="")
):
    for tool in TOOLS:
        if tool["id"] == tool_id:
            item = {
                "id": tool["id"],
                "name": tool["name"],
                "category": tool["category"],
                "difficulty": tool["difficulty"],
            }

            if include_description:
                item["description"] = tool["description"]

            return {"data": item}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tool not found")


@app.post("/tools", status_code=status.HTTP_201_CREATED)
def create_tool(tool: dict = Body(...)):
    if (
        "name" not in tool
        or "category" not in tool
        or "difficulty" not in tool
        or "description" not in tool
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The name, category, difficulty and description is mandatory",
        )

    if not str(tool["name"]).strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="The name cannot be empty"
        )

    if not str(tool["category"]).strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The category cannot be empty",
        )
    if not str(tool["difficulty"]).strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The difficulty cannot be empty",
        )

    if not str(tool["description"]).strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The description cannot be empty",
        )

    new_id = (TOOLS[-1]["id"] + 1) if TOOLS else 1
    new_tool = {
        "id": new_id,
        "name": tool["name"],
        "category": tool["category"],
        "difficulty": tool["difficulty"],
        "description": tool["description"],
    }

    TOOLS.append(new_tool)

    return {"message": "Created tool successfuly", "tool": new_tool}


@app.put("/tools/{tool_id}")
def update_tool(tool_id: int, data: dict = Body(...)):
    if (
        "name" not in data
        or "category" not in data
        or "difficulty" not in data
        or "description" not in data
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The name, category, difficulty and description is mandatory",
        )

    if not str(data["name"]).strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="The name cannot be empty"
        )

    if not str(data["category"]).strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The category cannot be empty",
        )
    if not str(data["difficulty"]).strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The difficulty cannot be empty",
        )

    if not str(data["description"]).strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The description cannot be empty",
        )

    for tool in TOOLS:
        if tool["id"] == tool_id:
            tool["name"] = data["name"]
            tool["category"] = data["category"]
            tool["difficulty"] = data["difficulty"]
            tool["description"] = data["description"]

            return {"message": "Updated tool successfuly", "tool": tool}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tool not found")


@app.delete("/tools/{tool_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tool(tool_id: int):
    for index, tool in enumerate(TOOLS):
        if tool["id"] == tool_id:
            TOOLS.pop(index)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tool not found")
