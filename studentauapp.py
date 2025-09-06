import streamlit as st

# ---------------------------
# Functions
# ---------------------------
def convert_aim(aim):
    if aim=='o':
        return 90
    elif aim=='a+':
        return 80
    elif aim=='a':
        return 70
    elif aim=='b+':
        return 60
    elif aim=='b':
        return 50
    elif aim=='c':
        return 45
    else:
        return "Invalid Input"
def getaim(int,aim):
    y=aim-int
    x=y/0.6
    return x
def grade(a):
    if 90 <= a <= 100:
        return " Your Predicted Grade: O or A+ 🎉"
    elif 80 <= a < 90:
        return " Your Predicted Grade: A+ or A 🥳"
    elif 70 <= a < 80:
        return " Your Predicted Grade: A or B+ 🎉"
    elif 60 <= a < 70:
        return " Your Predicted Grade: B+ or B 🥳"
    elif 50 <= a < 60:
        return " Your Predicted Grade: B or C 🙂"
    elif a < 50:
        return "⚠️ Your Predicted Grade: U (Needs Improvement)"
    else:
        return "❌ Invalid Input"

def calc_academic_level(p, q, r, s, present, total):
    set1 = p + (q * 0.6)

    if r == 0 and s == 0:
        avg_marks = round(set1)
    else:
        set2 = r + (s * 0.6)
        avg_marks = round((set1 + set2) / 2)

    if present<=total :
        att_per = round((present / total) * 100)
        return round((avg_marks + att_per) / 2)
    else:
        return "Invalid Input"

def calc_attendance_percentage(present, total):
    if present<=total :
        return round((present / total) * 100)
    else:
        return "Invalid Input"

def calc_internal_marks(p, q, r, s):
    set1 = p + (q * 0.6)

    if r == 0 and s == 0:
        int1 = round(set1 * 0.2)
        int2 = 0
        total_int = int1
    else:
        set2 = r + (s * 0.6)
        int1 = round(set1 * 0.2)
        int2 = round(set2 * 0.2)
        total_int = int1 + int2

    return int1, int2, total_int

# ---------------------------
# Streamlit UI
# ---------------------------

st.set_page_config(page_title="🎓 Student Helper App", page_icon="📘", layout="centered")

st.markdown("<h1 style='text-align:center; color:#1E90FF;'>🎓 Student Helper App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Your academic companion to calculate internal marks, attendance, and future grades!</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>( Turn Mobile For Better Experience )</p>", unsafe_allow_html=True)

name = st.text_input("👤 Enter your Name").capitalize()



task = st.selectbox(
    "📌 Choose a Task",
    ["-- Tap To Select -- 👇🏻", "Calculate Academic Level 🏅", "Future Grade Prediction 🔮", "Calculate Attendance Percentage 📅", "Calculate Internal Marks 🎯","Achieve Target 🚀"]
)

help=st.button("Instructions to Use App")
if help:
    st.title("Welcome Dude !!!")
    st.header("Instructions for Each Task below : ")

    st.subheader(" 1) Calculate Academic Level ")
    st.write(" * Enter Internal marks (?/40) of IAT exam and MODEL exam ")
    st.write(" * Enter Exam Marks (?/100) of IAT exam and MODEL exam ")
    st.write(" * If you didn't have MODEL exam marks just put 0")
    st.write(" * Next Enter No.Of.Classes present and Total No.Of.Classes ")
    st.write(" * Finally, Tap Calculate Button to see the Academic Level ")
    st.subheader(" 2) Future Grade Prediction ")
    st.write(" * Select Yes if you know your Academic level  And Enter it ")
    st.write(" * Select No if you dont know your Academic Level ")
    st.write(" * Similar Like Academic level Instruction ")
    st.write(" * New one is Enter your Coaching Class marks (?/100) ")
    st.write(" * Tap Predict Button to see the Predicted Grade in End Semester ")
    st.subheader(" 3) Attendance Percentage ")
    st.write(" * Enter Your No.Of.Classes Present ")
    st.write(" * Enter Your Total No.Of.Classes ")
    st.write(" * Tap Calculate Button to see the Attendance percentage ")
    st.subheader(" 4) Internal Marks ")
    st.write(" * Enter Internal marks (?/40) of IAT exam and MODEL exam ")
    st.write(" * Enter Exam Marks (?/100) of IAT exam and MODEL exam ")
    st.write(" * If you didn't have MODEL exam marks Just Put 0")
    st.write(" * Tap Calculate button to see the Internal marks of IAT,MODEL,END SEMESTER exams ")
    st.subheader(" 5) Achieve Target ")
    st.write(" * Enter Your End Semester Internal Mark (?/40) ")
    st.write(" * Select Your Target Grade like O,A+,A,B+,B,C .")
    st.write(" * Tap Calculate Button to see the Needed Marks in End Semester Exam")
    st.header("This app is very easy to use 👆🏻 ")

    

 
st.markdown("---")

# Task: Academic Level
if task == "Calculate Academic Level 🏅":
    st.subheader("📊 Academic Level Calculator")
    col1, col2 = st.columns(2)
    with col1:
        p = st.number_input("Internal (IAT) mark /40", min_value=0, max_value=40)
        q = st.number_input("IAT mark /100", min_value=0, max_value=100)
    with col2:
        r = st.number_input("Internal (Model) mark /40 (Enter 0 if not available)", min_value=0, max_value=40)
        s = st.number_input("Model mark /100 (Enter 0 if not available)", min_value=0, max_value=100)

    present = st.number_input("📅 No. of Present Classes", min_value=0)
    total = st.number_input("📚 Total Classes", min_value=0)

    if st.button("✅ Calculate Academic Level"):
        academic_level = calc_academic_level(p, q, r, s, present, total)
        if academic_level=="Invalid Input":
            st.subheader("Pls Enter the Correct Input ( Error: present>total )")
        else:
            st.success(f"🎯 {name}, Your Academic Level is: {academic_level}%")
            st.markdown("<h4 style='color:#00FFFF;'>Thanks for using the Student Helper App! 💫</h4>", unsafe_allow_html=True)

# Task: Grade Prediction
elif task == "Future Grade Prediction 🔮":
    st.subheader("🔮 Future Grade Predictor")
    method = st.radio("Do you know your Academic Level?", ["Yes", "No"])

    if method == "Yes":
        g = st.number_input("Enter your Academic Level", min_value=0, max_value=100)
        st.markdown("### 🧪 Coaching Class Marks")
        add = []
        for i in range(1, 3):
            coach = st.number_input(f"Phase {i} Coaching Marks /100", min_value=0, max_value=100, key=f"coach_{i}")
            add.append(coach)

        if st.button("🔍 Predict Grade"):
            avg_coach = round(sum(add) / 2)
            final_level = round((g + avg_coach) / 2)
            st.info(grade(final_level))
            st.success(f"All the best, {name}! 💐")
            st.markdown("<h4 style='color:#00FFFF;'>Thanks for using the Student Helper App! 💫</h4>", unsafe_allow_html=True)

    elif method == "No":
        st.markdown("### 📄 Enter Internal & Attendance Details")
        col1, col2 = st.columns(2)
        with col1:
            p = st.number_input("Internal (IAT) mark /40", min_value=0, max_value=40)
            q = st.number_input("IAT mark /100", min_value=0, max_value=100)
        with col2:
            r = st.number_input("Internal (Model) mark /40 (Enter 0 if not available)", min_value=0, max_value=40)
            s = st.number_input("Model mark /100 (Enter 0 if not available)", min_value=0, max_value=100)

        present = st.number_input("📅 No. of Present Classes", min_value=0)
        total = st.number_input("📚 Total Classes", min_value=0)

        if present>total :
            st.subheader("Pls Enter the correct Input ( Error: present>total )")
        else:
            st.markdown("### 🧪 Coaching Class Marks")
            add = []
            for i in range(1, 3):
                coach = st.number_input(f"Phase {i} Coaching Marks /100", min_value=0, max_value=100, key=f"coachn_{i}")
                add.append(coach)

            if st.button("🔍 Predict Grade"):
                academic_level = calc_academic_level(p, q, r, s, present, total)
                avg_coach = round(sum(add) / 2)
                final_level = round((academic_level + avg_coach) / 2)
                st.info(grade(final_level))
                st.success(f"All the best, {name}! 🌟")
                st.markdown("<h4 style='color:#00FFFF;'>Thanks for using the Student Helper App! 💫</h4>", unsafe_allow_html=True)

# Task: Attendance
elif task == "Calculate Attendance Percentage 📅":
    st.subheader("📅 Attendance Percentage Calculator")
    present = st.number_input("Number of Classes Attended", min_value=0)
    total = st.number_input("Total Number of Classes", min_value=0)

    if st.button("📈 Calculate Attendance"):
        att_per = calc_attendance_percentage(present, total)
        if att_per=="Invalid Input":
            st.subheader("Pls Enter the Correct Input ( Error: present>total )")
        else:
            st.success(f"{name}, Your Attendance Percentage is: {att_per}% 🎯")
            st.markdown("<h4 style='color:#00FFFF;'>Thanks for using the Student Helper App! 💫</h4>", unsafe_allow_html=True)

# Task: Internal Marks
elif task == "Calculate Internal Marks 🎯":
    st.subheader("📝 Internal Marks Calculator")
    col1, col2 = st.columns(2)
    with col1:
        p = st.number_input("Internal (IAT) mark /40", min_value=0, max_value=40)
        q = st.number_input("IAT mark /100", min_value=0, max_value=100)
    with col2:
        r = st.number_input("Internal (Model) mark /40 (Enter 0 if not available)", min_value=0, max_value=40)
        s = st.number_input("Model mark /100 (Enter 0 if not available)", min_value=0, max_value=100)

    if st.button("🧮 Calculate Internal Marks"):
        int1, int2, total_int = calc_internal_marks(p, q, r, s)
        st.info(f"📘 IAT Internal Marks (/20): {int1}")
        st.info(f"📗 Model Internal Marks (/20): {int2}")
        st.success(f"📙 Total Internal Marks (for End Semester): {total_int}")
        st.markdown("<h4 style='color:#00FFFF;'>Thanks for using the Student Helper App! 💫</h4>", unsafe_allow_html=True)
elif task=="Achieve Target 🚀":
    st.subheader("🎯 Achieve Your Grade")
    internal=st.number_input("End semester Internal Marks",min_value=0,max_value=40)
    aims=st.selectbox("Choose Grade 👇🏻",['O','A+','A','B+','B','C']).lower()
    aim=convert_aim(aims)
    if st.button("Calculate Need Marks ✅"):
        targ=round(getaim(internal,aim))
        if targ>100:
            st.success(f" {name} , It's impossible! But you get better 🌟")
            st.success("Try Again With less Target !!")
            st.markdown("<h4 style='color:#00FFFF;'>Thanks for using the Student Helper App! 💫</h4>", unsafe_allow_html=True)
        elif targ>=45:
            st.success(f" {name} , You Need (End Semester): {targ} 📈")
            st.markdown("<h4 style='color:#00FFFF;'>Thanks for using the Student Helper App! 💫</h4>", unsafe_allow_html=True)
        elif targ<45:
            st.success(f" {name}, You Need (End semester): {targ} 📈")
            st.success("According  to rules, YOU Must Want 45+ to PASS 🍀")
            st.markdown("<h4 style='color:#00FFFF;'>Thanks for using the Student Helper App! 💫</h4>", unsafe_allow_html=True)


# Background image set panna
page_bg = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("https://png.pngtree.com/background/20210714/original/pngtree-hand-drawn-lineart-education-blackboard-school-supplies-background-picture-image_1220253.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)







