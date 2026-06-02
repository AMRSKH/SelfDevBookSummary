import os

def generate_readme():
    # ទីនេះជាកន្លែងរៀបចំផ្នែកក្បាល (Header) នៃ README.md របស់អ្នក
    readme_content = """# គម្រោងប្រមូលផ្តុំឯកសារ (My Document Repository)

ទំព័រ README នេះត្រូវបានធ្វើបច្ចុប្បន្នភាពដោយស្វ័យប្រវត្តិចេញពីឯកសារ Markdown ទាំងអស់ដែលមាននៅក្នុង Repository នេះ។

---
"""
    
    # ស្វែងរកឯកសារ .md ទាំងអស់ (លើកលែងតែ README.md ខ្លួនឯង)
    for file in sorted(os.listdir('.')):
        if file.endswith('.md') and file.lower() != 'readme.md':
            # បង្កើតចំណងជើងរងដោយយកឈ្មោះឯកសារមកកែសម្រួល
            title = file.replace('.md', '').replace('_', ' ').title()
            readme_content += f"\n## ខ្លឹមសារពី៖ {title}\n\n"
            
            # អានខ្លឹមសារក្នុងឯកសារ .md នោះមកបញ្ចូល
            with open(file, 'r', encoding='utf-8') as f:
                readme_content += f.read()
            
            readme_content += "\n\n---\n"

    # សរសេរទិន្នន័យទាំងអស់ចូលទៅក្នុងឯកសារ README.md
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)

if __name__ == "__main__":
    generate_readme()
