# Course FAQ Chatbot — Starter tuần 1

## Mục tiêu
Tạo repo, kiến trúc, 12 FAQ minh họa (chưa kiểm chứng theo môn cụ thể), giao diện web mẫu, Lambda healthcheck, chuẩn bị AWS resources.

## AWS setup (Learner Lab)
1. Start Lab; mở AWS Console; chọn **us-east-1**.
2. S3: tạo bucket `course-faq-web-<unique>` cho frontend; bucket `course-faq-data-<unique>` cho `faq.json`. Dữ liệu phải PRIVATE.
3. DynamoDB: tạo bảng `CourseFAQQueryLogs`, partition key `requestId` (String), on-demand nếu lab cho phép.
4. Lambda: Create function → Author from scratch → `course-faq-health` → Python 3.x được hỗ trợ → Change default execution role → **Use existing role: LabRole**; dán `lambda/lambda_function.py`; Deploy; Test `{}`.
5. API Gateway: HTTP API `course-faq-api` → integration Lambda → route `GET /health` → stage `$default` auto-deploy → test `/health`.
6. Gắn tags Project=CourseFAQChatbot; Owner=<mã thành viên/nhóm> cho các tài nguyên hỗ trợ tagging.
7. S3 web: bật Static website hosting, index.html; chỉ cho phép đọc public các file web nếu chính sách lab cho phép; upload 3 file frontend. Không public bucket dữ liệu.
8. Chụp ảnh AWS Console có account ID, Region và thời gian; ghi worklog giờ thực tế.

## Kiểm thử local
`python -m unittest discover -s tests` (cần sửa test sang unittest nếu dùng lệnh này), hoặc `pytest -q` nếu có pytest.

## Lưu ý
S3 website endpoint là HTTP (không HTTPS); production muốn HTTPS nên cần CloudFront hoặc giải pháp proxy phù hợp, nhưng phải đối chiếu các dịch vụ được phép. FAQ mẫu chỉ minh họa, không đại diện đề cương môn học thật.
