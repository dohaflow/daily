@echo off
chcp 65001 > nul
title ★...싸이월드 감성 다이어트 미니홈피...★

echo ========================================================
echo   ★... 싸이월드 감성 다이어트 미니홈피 실행기 ...★
echo   도토리(🌰) 모으며 완성하는 즐거운 나만의 다이어트!
echo ========================================================

where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    echo Python 웹 서버 모드로 미니홈피를 구동합니다...
    python run.py
) else (
    echo 브라우저에서 바로 index.html 파일을 실행합니다...
    start index.html
)
