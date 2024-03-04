!pip install -r requirements.txt

import os
import re
import PyPDF2
import openai
import plotly.graph_objs as go
import gradio as gr

class ResumeAnalyzer:
    def __init__(self, key):
        self.key = key
        openai.api_key = key

    def extract_text_from_file(self, file_path):
        file_extension = file_path.split('.')[-1]

        if file_extension == 'pdf':
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                extracted_text = ""
                for page_number in range(len(reader.pages)):
                    page = reader.pages[page_number]
                    extracted_text += page.extract_text()
            return extracted_text
        elif file_extension == 'txt':
            with open(file_path, 'r') as file:
                return file.read()
        else:
            return "Desteklenmeyen dosya türü"

    def response_from_ai(self, textjd, textcv):
        job_description = self.extract_text_from_file(textjd)
        resume = self.extract_text_from_file(textcv)

        prompt = f"""
Given the job description and the resume, assess the matching percentage to 100 and if 100 percentage not matched mention the remaining percentage with reason.

**Job Description: {job_description}**
**Resume: {resume}**

Detailed Analysis:
Matched Percentage: [matching percentage].
Reason: [Detail the reason and keys to obtain this matching percentage from the job description and resume](min 30 words).
Keywords: [matched key words from {job_description} and {resume}](max 10 words).
Information Candidate: [Matching from {resume} extract this information
                        Name:
                        Education:
                        Mail Address:
                        City:](max 100 characters).


              """
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}], temperature=0.8,
  max_tokens=400,
  top_p=1)
        generated_text = completion.choices[0].message.content
        return generated_text

    def matching_percentage(self, job_description_path, resume_path):
        job_description_path = job_description_path
        resume_path = resume_path

        generated_text = self.response_from_ai(job_description_path, resume_path)
        print("generated_text")

        result = generated_text
        lines = result.split('\n')

        matched_percentage = None
        matched_percentage_txt = None
        reason = None
        keywords = None
        information_candidate = None

        for line in lines:
            if line.startswith('Matched Percentage:'):
                match = re.search(r"Matched Percentage: (\d+)%", line)
                if match:
                    matched_percentage = int(match.group(1))
                    matched_percentage_txt = (f"Matched Percentage: {matched_percentage}%")
            elif line.startswith('Reason'):
                reason = line.split(':')[1].strip()
            elif line.startswith('Keywords'):
                keywords = line.split(':')[1].strip()
            elif line.startswith('Information Candidate'):
                information_candidate = line.split(':')[1].strip()

        labels = ['Matched', 'Remaining']
        values = [matched_percentage, 100 - matched_percentage]

        # Renkli bir palet kullanarak pasta grafiğini oluştur
        colors = ['#1f77b4', '#ff7f0e']  # Renk paleti örneği, burada mavi ve turuncu renkler kullanıyoruz

        fig = go.Figure(data=[go.Pie(labels=labels, values=values, marker=dict(colors=colors))])
        return matched_percentage_txt, reason, keywords, information_candidate, fig


    def gradio_interface(self):
      with gr.Blocks(css="style.css",theme='karthikeyan-adople/hudsonhayes-gray') as app:
          gr.HTML("""<center class="darkblue" style='background-color:rgb(0,1,36); text-align:center;padding:30px;'><center>
          <img class="leftimage" align="left" src="https://r.resimlink.com/BKHJ4.png" alt="Image" width="210" height="210">
          <h1 class ="center" style="color:#fff">Burak Öksüz</h1></center>
          <br><center><h1 style="color:#fff">Resume Analyser</h1></center>""")


          with gr.Row():
              with gr.Column(scale=1.0, min_width=150, ):
                    jobDescription = gr.File(label="Job Description")
              with gr.Column(scale=1.0, min_width=150):
                    resume = gr.File(label="Resume")
              with gr.Column(scale=1.0, min_width=150):
                    analyse = gr.Button("Analyse")
          with gr.Row():
              with gr.Column(scale=1.0, min_width=150):
                    perncentage = gr.Textbox(label="Matching Percentage", lines=8)
              with gr.Column(scale=1.0, min_width=150):
                    reason = gr.Textbox(label="Matching Reason", lines=8)
              with gr.Column(scale=1.0, min_width=150):
                    keywords = gr.Textbox(label="Matched Keywords", lines=8)
              with gr.Column(scale=1.0, min_width=150):
                    information_candidate = gr.Textbox(label="Information Candidate", lines=8)
          with gr.Row():
              with gr.Column(scale=1.0, min_width=150):
                  pychart = gr.Plot(label="Matching Percentage Chart")
          analyse.click(self.matching_percentage, [jobDescription, resume], [perncentage,reason,keywords,information_candidate,pychart])

      app.launch()

# Ana kod
if __name__ == "__main__":
    key = "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"
    analyzer = ResumeAnalyzer(key)
    analyzer.gradio_interface()

