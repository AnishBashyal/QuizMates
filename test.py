# quizSocket.on("displayTable", (data) => {
# //   console.log(data[0], data[1], data[2]);
# //   let index = 0;
# //   table = document.getElementById("leaderboardtable");
# //   table.innerHTML = "";
# //   for (const team_code of data[2]) {
# //     index++;
# //     const team_name = data[1][team_code][0];
# //     const score = data[0][team_code];
# //     //   const u_sid = Object.keys(item)[0];
# //     //   const u_name = Object.values(item)[0];

# //     const tr = document.createElement("tr");

# //     const th = document.createElement("th");
# //     th.scope = "row";
# //     th.textContent = index;
# //     tr.appendChild(th);

# //     const td1 = document.createElement("td");
# //     td1.textContent = team_name;

# //     tr.appendChild(td1);

# //     const td2 = document.createElement("td");
# //     td2.textContent = score;
# //     tr.appendChild(td2);

# //     table.appendChild(tr);
# //   }
# // });


# <!-- {% extends "layout.html" %} {% block body %}
# <h1>Create Team</h1>

# <form method="post" action="{{url_for('team_room.create_team')}}">
#   <div>
#     <input type="text" placeholder="Pick a name" name="name" required />
#     <input
#       type="text"
#       placeholder="Enter your team name"
#       name="team_name"
#       required
#     />
#     <button type="submit">Create Team</button>
#   </div>
# </form>

# <form method="post" action="{{url_for('team_room.join_team')}}">
#   <div>
#     <input type="text" placeholder="Pick a name" name="name" required />
#     <input
#       type="text"
#       placeholder="Enter your team code"
#       name="team_code"
#       required
#     />

#     <button type="submit">Join Team</button>
#   </div>
# </form>
# -->
