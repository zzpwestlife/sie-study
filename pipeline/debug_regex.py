import re

content = """<div class="block list-item" id="block-4406612688">
<div class="block-en">• Notification (registration by filing): Notification is the simplest form of registration for</div>
<div class="block-zh missing-trans">[Missing Translation]</div>
</div>"""

block_id = "block-4406612688"
pattern = r'(<(section|div)[^>]*id="' + re.escape(block_id) + r'"[^>]*>.*?)(<(p|div) class="block-zh missing-trans">)(.*?)(<\/\4>)'

match = re.search(pattern, content, flags=re.DOTALL)
if match:
    print("Match found!")
    print("Group 1:", match.group(1))
    print("Group 2:", match.group(2))
    print("Group 3:", match.group(3))
    print("Group 4:", match.group(4))
    print("Group 5:", match.group(5))
    print("Group 6:", match.group(6))
else:
    print("No match found.")
