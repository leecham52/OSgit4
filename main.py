"""
20161090 이채민 과제 4
폴더 자동 정리 프로그램
"""
import os

#여러 파일을 형태 별로 구분을 시킬 것이기 때문에, . 뒤에 적힌 것들을 미리 확인하기 위한 grouping
groups = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Docs": [".pdf", ".docx", ".hwp", ".txt", ".xlsx", ".ppt", ".pptx"],
    "Code": [".py", ".c", ".cpp", ".dart", ".java"],
    "Video": [".mp4", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Zip": [".zip", ".tar", ".7z", ".gz"],
}

#input으로 들어오는 폴더 내 파일, 폴더 확인 및 파일만을 return
def check_folder_choose_files(folder_path):
    #폴더 내부 파일, 폴더 리스트 list[] 형태로 저장
    folder_list = os.listdir(folder_path)
    files = []
    for something in folder_list:
        something_path = os.path.join(folder_path, something)
        if os.path.isfile(something_path):
            files.append(something_path)
    return files
