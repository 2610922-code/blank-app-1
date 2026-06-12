import streamlit as st

# 웹 페이지 제목 설정
st.title("🚗 차량별 요금 계산기")
st.write("차종과 할인 조건을 선택하시면 최종 요금을 계산해 드립니다.")

st.markdown("---")

# 1. 차종 선택 (기존 코드의 C, F 리스트 활용 및 구조화)
car_type = st.radio(
    "차량 종류를 선택하세요:",
    ["경차 (기본 요금: 1,000원)", "일반차 (기본 요금: 2,000원)"]
)

# 차종에 따른 기본 요금(fee) 설정
if "경차" in car_type:
    base_fee = 1000
else:
    base_fee = 2000

# 2. 추가 할인 선택 (기존 코드의 할인 입력 및 20% 할인 로직 반영)
discount_option = st.selectbox(
    "추가 할인 혜택을 선택하세요:",
    ["선택 안 함 (0%)", "특별 할인 (20% 할인)"]
)

# 요금 계산 로직
final_fee = base_fee
if "특별 할인" in discount_option:
    final_fee = int(base_fee * 0.8) # 20% 할인 적용

# 3. 결과 출력
st.markdown("---")
st.subheader("📊 계산 결과")
st.metric(label="최종 요금", value=f"{final_fee:,} 원")

# 시각적인 피드백 추가
st.success(f"선택하신 {car_type.split(' ')[0]}의 최종 요금은 **{final_fee:,}원**입니다.")