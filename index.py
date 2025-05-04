import streamlit as st

# Page settings
st.set_page_config(page_title="📝 Daily Task Planner", page_icon="📅", layout="centered")

# Title
st.title("📝 Daily Task Planner")
st.subheader("Plan your day with ease! 🌞")

# Initialize session state for tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Add a new task
new_task = st.text_input("Enter a new task:")

if st.button("➕ Add Task"):
    if new_task:
        st.session_state.tasks.append({"task": new_task, "done": False})
        st.success("Task added!")

st.markdown("---")

# Display tasks with checkboxes
st.header("📋 Today's Tasks")
for i, task in enumerate(st.session_state.tasks):
    checked = st.checkbox(task["task"], value=task["done"], key=i)
    st.session_state.tasks[i]["done"] = checked

# Option to clear all tasks
if st.button("🗑️ Clear All Tasks"):
    st.session_state.tasks = []
    st.warning("All tasks cleared.")

# Footer
st.markdown("---")
st.info("Keep going, Code Queen! You're doing amazing work today. 💪👑")
