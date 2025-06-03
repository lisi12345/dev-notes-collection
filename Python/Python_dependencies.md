# Pylint
Generate .pylintrc file
> pylint --generate-rcfile | out-file -encoding utf8 .pylintrc

# requirements.txt
> py -m pip install -U pipreqs
> python -m  pipreqs.pipreqs src --savepath requirements.txt --force

To ignore `.venv` folder:
> pipreqs . --force --ignore .venv

A batch file to get all denpendencies across code and test folder:
> @ECHO OFF
@REM py -m pip install -U pipreqs
@REM python -m  pipreqs.pipreqs src --savepath srcrequirements.txt --force
@REM python -m  pipreqs.pipreqs test --savepath testrequirements.txt --force
@REM cat srcrequirements.txt testrequirements.txt | sort -u > mergerequirements.txt
type @("srcrequirements.txt", "testrequirements.txt") | sort > mergerequirements.txt
findstr /v /i /L /c:"auto_mix_prep" mergerequirements.txt > requirements.txt
@REM del /s /q srcrequirements.txt
@REM del /s /q testrequirements.txt
@REM del /s /q mergerequirements.txt
pause
Get-Content mergerequirements.txt | Sort-Object -Unique | Set-Content requirements.txt
