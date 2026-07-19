# import streamlit as st
# import pandas as pd
# import joblib

# # Load Models & Scaler
# enrollment_model = joblib.load("enrollment_model.pkl")
# revenue_model = joblib.load("revenue_model.pkl")
# scaler = joblib.load("scaler.pkl")

# st.title("EduPro Course Demand & Revenue Forecasting")

# # Inputs
# course_price = st.number_input(
#     "Course Price",
#     min_value=0.0,
#     value=500.0
# )

# course_duration = st.number_input(
#     "Course Duration",
#     min_value=1.0,
#     value=20.0
# )

# course_rating = st.slider(
#     "Course Rating",
#     1.0,
#     5.0,
#     4.0
# )

# teacher_rating = st.slider(
#     "Teacher Rating",
#     1.0,
#     5.0,
#     4.0
# )

# experience = st.number_input(
#     "Years Of Experience",
#     min_value=0,
#     value=5
# )

# course_level = st.selectbox(
#     "Course Level",
#     ["Beginner", "Intermediate", "Advanced"]
# )

# course_category = st.selectbox(
#     "Course Category",
#     [
#         "Business",
#         "Cybersecurity",
#         "Data Science",
#         "Design",
#         "Digital Marketing",
#         "Finance",
#         "Machine Learning",
#         "Marketing",
#         "Programming",
#         "Project Management",
#         "Web Development"
#     ]
# )

# course_type = st.selectbox(
#     "Course Type",
#     ["Free", "Paid"]
# )

# if st.button("Predict"):

#     # Level Encoding
#     level_map = {
#         "Beginner": 0,
#         "Intermediate": 1,
#         "Advanced": 2
#     }

#     course_level_encoded = level_map[course_level]

#     # Feature Engineering

#     price_band_low = 1 if course_price < 500 else 0

#     duration_bucket_medium = (
#         1 if 20 <= course_duration <= 40 else 0
#     )

#     duration_bucket_short = (
#         1 if course_duration < 20 else 0
#     )

#     rating_tier_excellent = (
#         1 if course_rating >= 4.5 else 0
#     )

#     rating_tier_good = (
#         1 if 3.5 <= course_rating < 4.5 else 0
#     )

#     # Base DataFrame
#     input_df = pd.DataFrame({
#         "CoursePrice": [course_price],
#         "CourseDuration": [course_duration],
#         "CourseRating": [course_rating],
#         "TeacherRating": [teacher_rating],
#         "YearsOfExperience": [experience],
#         "CourseLevelEncoded": [course_level_encoded]
#     })

#     # Category Dummies
#     categories = [
#         "Business",
#         "Cybersecurity",
#         "Data Science",
#         "Design",
#         "Digital Marketing",
#         "Finance",
#         "Machine Learning",
#         "Marketing",
#         "Programming",
#         "Project Management",
#         "Web Development"
#     ]

#     for cat in categories:
#         input_df[f"CourseCategory_{cat}"] = (
#             1 if course_category == cat else 0
#         )

#     # Course Type
#     input_df["CourseType_Paid"] = (
#         1 if course_type == "Paid" else 0
#     )

#     # Engineered Features
#     input_df["PriceBand_Low"] = price_band_low
#     input_df["DurationBucket_Medium"] = duration_bucket_medium
#     input_df["DurationBucket_Short"] = duration_bucket_short
#     input_df["RatingTier_Excellent"] = rating_tier_excellent
#     input_df["RatingTier_Good"] = rating_tier_good

#     # Missing columns from training
#     input_df["RevenuePerEnrollment"] = 0
#     input_df["PastAverageRevenue"] = 0

#     # Scale numeric columns
#     numeric_cols = [
#         "CoursePrice",
#         "CourseDuration",
#         "CourseRating",
#         "TeacherRating",
#         "YearsOfExperience",
#         # "RevenuePerEnrollment",
#         # "PastAverageRevenue"
#     ]

#     input_df[numeric_cols] = scaler.transform(
#         input_df[numeric_cols]
#     )

#     # Reorder columns exactly like training
#     input_df = input_df[
#         [
#             'CoursePrice',
#             'CourseDuration',
#             'CourseRating',
#             'TeacherRating',
#             'YearsOfExperience',
#             'CourseLevelEncoded',
#             'CourseCategory_Business',
#             'CourseCategory_Cybersecurity',
#             'CourseCategory_Data Science',
#             'CourseCategory_Design',
#             'CourseCategory_Digital Marketing',
#             'CourseCategory_Finance',
#             'CourseCategory_Machine Learning',
#             'CourseCategory_Marketing',
#             'CourseCategory_Programming',
#             'CourseCategory_Project Management',
#             'CourseCategory_Web Development',
#             'CourseType_Paid',
#             'PriceBand_Low',
#             'DurationBucket_Medium',
#             'DurationBucket_Short',
#             'RatingTier_Excellent',
#             'RatingTier_Good'
#         ]
#     ]

#     # Predictions
#     enrollment_prediction = enrollment_model.predict(
#         input_df
#     )[0]

#     revenue_prediction = revenue_model.predict(
#         input_df
#     )[0]

#     st.subheader("Prediction Results")

#     st.success(
#         f"Predicted Enrollment Count: {round(enrollment_prediction)}"
#     )

#     st.success(
#         f"Predicted Revenue: ₹ {revenue_prediction:,.2f}"
#     )


import streamlit as st
import pandas as pd
import joblib

# Load Models & Scaler
enrollment_model = joblib.load("enrollment_model.pkl")
revenue_model = joblib.load("revenue_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("EduPro Course Demand & Revenue Forecasting")

# Inputs
course_price = st.number_input(
    "Course Price",
    min_value=0.0,
    value=500.0
)

course_duration = st.number_input(
    "Course Duration",
    min_value=1.0,
    value=20.0
)

course_rating = st.slider(
    "Course Rating",
    1.0,
    5.0,
    4.0
)

teacher_rating = st.slider(
    "Teacher Rating",
    1.0,
    5.0,
    4.0
)

experience = st.number_input(
    "Years Of Experience",
    min_value=0,
    value=5
)

course_level = st.selectbox(
    "Course Level",
    ["Beginner", "Intermediate", "Advanced"]
)

course_category = st.selectbox(
    "Course Category",
    [
        "Business",
        "Cybersecurity",
        "Data Science",
        "Design",
        "Digital Marketing",
        "Finance",
        "Machine Learning",
        "Marketing",
        "Programming",
        "Project Management",
        "Web Development"
    ]
)

course_type = st.selectbox(
    "Course Type",
    ["Free", "Paid"]
)

if st.button("Predict"):

    # Level Encoding
    level_map = {
        "Beginner": 0,
        "Intermediate": 1,
        "Advanced": 2
    }

    course_level_encoded = level_map[course_level]

    # Feature Engineering
    price_band_low = 1 if course_price < 500 else 0

    duration_bucket_medium = (
        1 if 20 <= course_duration <= 40 else 0
    )

    duration_bucket_short = (
        1 if course_duration < 20 else 0
    )

    rating_tier_excellent = (
        1 if course_rating >= 4.5 else 0
    )

    rating_tier_good = (
        1 if 3.5 <= course_rating < 4.5 else 0
    )

    # Base DataFrame
    input_df = pd.DataFrame({
        "CoursePrice": [course_price],
        "CourseDuration": [course_duration],
        "CourseRating": [course_rating],
        "TeacherRating": [teacher_rating],
        "YearsOfExperience": [experience],
        "CourseLevelEncoded": [course_level_encoded]
    })

    # Category Dummies
    categories = [
        "Business",
        "Cybersecurity",
        "Data Science",
        "Design",
        "Digital Marketing",
        "Finance",
        "Machine Learning",
        "Marketing",
        "Programming",
        "Project Management",
        "Web Development"
    ]

    for cat in categories:
        input_df[f"CourseCategory_{cat}"] = (
            1 if course_category == cat else 0
        )

    # Course Type
    input_df["CourseType_Paid"] = (
        1 if course_type == "Paid" else 0
    )

    # Engineered Features
    input_df["PriceBand_Low"] = price_band_low
    input_df["DurationBucket_Medium"] = duration_bucket_medium
    input_df["DurationBucket_Short"] = duration_bucket_short
    input_df["RatingTier_Excellent"] = rating_tier_excellent
    input_df["RatingTier_Good"] = rating_tier_good

    # Temporary columns for scaler
    input_df["RevenuePerEnrollment"] = 0
    input_df["PastAverageRevenue"] = 0

    # Scale columns exactly like training
    numeric_cols = [
        "CoursePrice",
        "CourseDuration",
        "CourseRating",
        "TeacherRating",
        "YearsOfExperience",
        "RevenuePerEnrollment",
        "PastAverageRevenue"
    ]

    input_df[numeric_cols] = scaler.transform(
        input_df[numeric_cols]
    )

    # Remove columns not used in training
    input_df.drop(
        columns=[
            "RevenuePerEnrollment",
            "PastAverageRevenue"
        ],
        inplace=True
    )

    # Feature order must match training
    input_df = input_df[
        [
            'CoursePrice',
            'CourseDuration',
            'CourseRating',
            'TeacherRating',
            'YearsOfExperience',
            'CourseLevelEncoded',
            'CourseCategory_Business',
            'CourseCategory_Cybersecurity',
            'CourseCategory_Data Science',
            'CourseCategory_Design',
            'CourseCategory_Digital Marketing',
            'CourseCategory_Finance',
            'CourseCategory_Machine Learning',
            'CourseCategory_Marketing',
            'CourseCategory_Programming',
            'CourseCategory_Project Management',
            'CourseCategory_Web Development',
            'CourseType_Paid',
            'PriceBand_Low',
            'DurationBucket_Medium',
            'DurationBucket_Short',
            'RatingTier_Excellent',
            'RatingTier_Good'
        ]
    ]

    # Predictions
    enrollment_prediction = enrollment_model.predict(
        input_df
    )[0]

    revenue_prediction = revenue_model.predict(
        input_df
    )[0]


    st.subheader("Prediction Results")

    st.success(
        f"Predicted Enrollment Count: {round(enrollment_prediction)}"
    )

    st.success(
        f"Predicted Revenue: ₹ {revenue_prediction:,.2f}"
    )