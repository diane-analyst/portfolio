"""
matplotlib 폰트 캐시를 삭제하는 스크립트
한글이 네모로 나올 때 실행하세요.
"""
import matplotlib
import matplotlib.font_manager as fm
import os
import shutil

# matplotlib 캐시 디렉토리 찾기
cache_dir = matplotlib.get_cachedir()
font_cache_dir = os.path.join(cache_dir, 'fontlist-v*.json')

print("matplotlib 폰트 캐시 삭제 중...")
print(f"캐시 디렉토리: {cache_dir}")

# 폰트 캐시 파일 삭제
try:
    # fontlist 파일 찾기
    if os.path.exists(cache_dir):
        for file in os.listdir(cache_dir):
            if file.startswith('fontlist'):
                file_path = os.path.join(cache_dir, file)
                os.remove(file_path)
                print(f"삭제됨: {file}")
    
    # 폰트 캐시 재구성
    print("\n폰트 캐시 재구성 중...")
    fm._rebuild()
    print("✅ 폰트 캐시 재구성 완료!")
    print("\n이제 노트북의 첫 번째 셀을 다시 실행하세요.")
    
except Exception as e:
    print(f"오류 발생: {e}")
    print("\n수동으로 캐시를 삭제하려면:")
    print(f"1. {cache_dir} 폴더를 열기")
    print("2. 'fontlist'로 시작하는 모든 파일 삭제")
    print("3. 노트북 재시작")

