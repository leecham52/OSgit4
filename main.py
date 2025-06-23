"""
20161090 이채민 과제 4
폴더 자동 정리 프로그램
"""

"""
초기는 데스크탑 폴더 내에 폴더들을 보여줌
정리하고 싶은 폴더를 입력
그 폴더 내에 파일들과 폴더들을 리스트 형태로 저장
파일들은 파일 형태 따라서 그 파일 형태에 맞는 폴더를 만들고, 폴더로 옮김
프로그램 종료
"""

import os

#기본 세팅은 바탕화면 내 폴더
DESKTOP = "C:/Users/LEE/Desktop"

#여러 파일을 형태 별로 구분을 시킬 것이기 때문에, . 뒤에 적힌 것들을 미리 확인하기 위한 grouping
groups = {
    "이미지": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "문서": [".pdf", ".docx", ".hwp", ".txt", ".xlsx", ".ppt", ".pptx"],
    "코드": [".py", ".c", ".cpp", ".dart", ".java"],
    "영상": [".mp4", ".avi"],
    "음악": [".mp3", ".wav"],
    "압축": [".zip", ".tar", ".7z", ".gz"],
}

#input으로 들어오는 폴더 내 파일, 폴더 확인 및 파일, 폴더 path 를 return
#input을 directory, output을 files, folders로 헷갈리지 않게 이름 지정
def check_directory(dir_path):
    #폴더 내부 파일, 폴더 리스트 list[] 형태로 저장
    files = []
    folders = []
    for f in os.listdir(dir_path):
        f_path = os.path.join(dir_path, f)
        if os.path.isfile(f_path):
            files.append(f_path) # 폴더 내 파일 path들을 리스트에 저장
        elif os.path.isdir(f_path):
            folders.append(f_path)# 폴더 내 폴더 path들을 리스트에 저장

    return files, folders

#groups에 있는 것들은 그 폴더가 생성이 되면서, 그 폴더에 들어가고, 확장자가 위에 없는 것들은 기타라는 폴더에 따로 넣어준다.
def classify_and_move_files(files, base_path):
    for file_path in files:
        # 파일의 확장자를 extension에 저장 및 소문자로 변환
        _, extension = os.path.splitext(file_path)
        extension = extension.lower()
        filename = os.path.basename(file_path) #파일 이름만 추출

        moved = False
        #미리 정의한 groups를 보고 비교분석
        for group_name, extensions in groups.items():
            if extension in extensions:
                target_folder = os.path.join(base_path, group_name)
                os.makedirs(target_folder, exist_ok=True)
                new_path = os.path.join(target_folder, filename)
                os.rename(file_path, new_path)
                moved = True
                break
        if not moved:
            # 확장자가 정의되지 않은 경우 기타로 이동
            target_folder = os.path.join(base_path, "기타")
            os.makedirs(target_folder, exist_ok=True)
            new_path = os.path.join(target_folder, filename)
            os.rename(file_path, new_path)



def main():
    
    print("바탕화면 내 폴더 목록: ")
    desktop_directories = []
    desktop_items = os.listdir(DESKTOP)
    for item in desktop_items:
        item_path = os.path.join(DESKTOP, item)
        if os.path.isdir(item_path):
            desktop_directories.append(item)
    for directory in desktop_directories:
        print(f"- {directory}")
        
    directory_name = input("정리할 폴더 이름을 써주세요.")
    directory_path = os.path.join(DESKTOP,directory_name)

    #폴더 예외처리
    if not os.path.exists(directory_path):
        print("해당 폴더는 존재하지 않습니다.")
        return
    if not os.path.isdir(directory_path):
        print("해당 이름은 폴더가 아닙니다.")
        return
    files, folders = check_directory(directory_path)
    print("폴더 내 파일들: ")
    for f in files:
        print(f"- {f}")
    print("폴더 내 폴더들: ")
    for f in folders:
        print(f"- {f}")

    classify_and_move_files(files, directory_path)
    print("정리가 끝났습니다.")

if __name__ == "__main__":
    main()