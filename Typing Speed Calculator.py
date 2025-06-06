import time

# 🎯 Target sentence
goal = "The quick brown fox jumps over the lazy dog"

# 🖐️ Welcome
print("="*50)
print("🧠  Typing Speed Challenge - Chanda Edition  💻")
print("="*50)
print("\nType the below sentence exactly as it is:\n")
print("👉", goal)
input("\n🎬 Hit Enter to begin...")

# ⏱️ Start time
begin = time.time()

# ✍️ Typing input
typed = input("\n⌨️ Start Typing Here:\n\n")

# 🕒 End time
finish = time.time()
duration = finish - begin
minutes = duration / 60

# 🧮 Count words
typed_words = len(typed.split())
speed = typed_words / minutes

# 🎯 Accuracy logic
def get_accuracy(original, typed):
    matched = sum(1 for a, b in zip(original, typed) if a == b)
    total = len(original)
    return round((matched / total) * 100, 2)

accuracy = get_accuracy(goal, typed)

# 📊 Result Display
print("\n" + "-"*50)
print(f"⏰ Time Taken: {round(duration, 2)} seconds")
print(f"🚀 Speed: {round(speed, 2)} words per minute (WPM)")
print(f"🎯 Accuracy: {accuracy}%")
print("-"*50)

# 🔍 Feedback
if speed >= 40 and accuracy >= 90:
    print("🌟 Outstanding! Fast and accurate.")
elif speed >= 30:
    print("💪 Good! You’re improving. Keep practicing.")
else:
    print("🛠️ Needs Practice. Try again tomorrow!")

# ⌛ Pause so output remains
input("\n🔚 Press Enter to close...")
a
