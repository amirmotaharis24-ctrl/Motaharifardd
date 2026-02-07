
# ============================================================================
# Smart Travel Planner - Re-structured Multi-Agent Architecture
# ============================================================================

from google.adk.agents.llm_agent import Agent

# ----------------------------------------------------------------------------
# Tools
# ----------------------------------------------------------------------------

def get_weather(city: str) -> str:
    return f"گزارش هواشناسی {city}: شرایط مناسب برای گردشگری."

# ----------------------------------------------------------------------------
# Intake Layer
# ----------------------------------------------------------------------------

user_profile_agent = Agent(
    name="Traveler_Profile_Collector",
    model="gemini-2.5-flash",
    instruction="""
اطلاعات مسافر را استخراج کنید:
- بودجه
- مدت سفر
- علایق گردشگری
- شرایط ویژه
پس از تکمیل، داده‌ها را ساختارمند ارسال کنید.
"""
)

# ----------------------------------------------------------------------------
# Research Layer
# ----------------------------------------------------------------------------

destination_agent = Agent(
    name="Destination_Researcher",
    model="gemini-2.5-flash",
    instruction="جاذبه‌های مهم مقصد را شناسایی و معرفی کنید."
)

transport_agent = Agent(
    name="Mobility_Guide",
    model="gemini-2.5-flash",
    instruction="روش‌های حمل‌ونقل و دسترسی به مکان‌ها را پیشنهاد دهید."
)

expense_agent = Agent(
    name="Expense_Planner",
    model="gemini-2.5-flash",
    instruction="برآورد هزینه‌های اقامت، غذا و گردش را محاسبه کنید."
)

# ----------------------------------------------------------------------------
# Planning Layer
# ----------------------------------------------------------------------------

daily_plan_agent = Agent(
    name="Daily_Trip_Planner",
    model="gemini-2.5-flash",
    instruction="برنامه روزانه سفر را طراحی کنید."
)

enrichment_agent = Agent(
    name="Plan_Enricher",
    model="gemini-2.5-flash",
    instruction="جزئیات دقیق فعالیت‌ها را به برنامه اضافه کنید."
)

# ----------------------------------------------------------------------------
# Review Layer
# ----------------------------------------------------------------------------

audit_agent = Agent(
    name="Travel_Auditor",
    model="gemini-2.5-flash",
    instruction="برنامه سفر را بررسی و نقاط ضعف را مشخص کنید."
)

refine_agent = Agent(
    name="Travel_Refiner",
    model="gemini-2.5-flash",
    instruction="برنامه را براساس گزارش ارزیابی اصلاح کنید."
)

# ----------------------------------------------------------------------------
# Coordinator
# ----------------------------------------------------------------------------

travel_master_agent = Agent(
    name="Travel_Master_Coordinator",
    model="gemini-2.5-flash",
    instruction="""
گزارش نهایی شامل موارد زیر باشد:
- برنامه کامل سفر
- معرفی جاذبه‌ها
- برآورد هزینه
- پیشنهاد حمل‌ونقل
- وضعیت آب‌وهوا
""",
    tools=[get_weather],
    sub_agents=[
        user_profile_agent,
        destination_agent,
        transport_agent,
        expense_agent,
        daily_plan_agent,
        enrichment_agent,
        audit_agent,
        refine_agent
    ]
)
