def fake_profile_score(profile):
    score = 0
    reasons = []

    # New account
    age_days = profile.get("account_age_days", 365)

    if age_days < 30:
        score += 30
        reasons.append("Very new account")

    # Follower/following ratio
    followers = profile.get("followers", 1)
    following = profile.get("following", 1)

    ratio = following / max(followers, 1)

    if ratio > 10:
        score += 25
        reasons.append("Very high following-to-follower ratio")

    # Profile picture
    if profile.get("no_profile_pic"):
        score += 20
        reasons.append("No profile picture")

    # Number of posts
    if profile.get("posts", 100) < 5:
        score += 15
        reasons.append("Very few posts")

    # Generic/default bio
    if profile.get("default_bio"):
        score += 10
        reasons.append("Generic/default bio")

    score = min(score, 100)

    if score >= 70:
        risk = "HIGH"
    elif score >= 40:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return score, risk, reasons


# Five anonymized practice profiles
profiles = [
    {
        "name": "Profile A",
        "account_age_days": 7,
        "followers": 2,
        "following": 900,
        "no_profile_pic": True,
        "posts": 1,
        "default_bio": True
    },
    {
        "name": "Profile B",
        "account_age_days": 1200,
        "followers": 4500,
        "following": 320,
        "no_profile_pic": False,
        "posts": 870,
        "default_bio": False
    },
    {
        "name": "Profile C",
        "account_age_days": 15,
        "followers": 8,
        "following": 250,
        "no_profile_pic": False,
        "posts": 3,
        "default_bio": True
    },
    {
        "name": "Profile D",
        "account_age_days": 600,
        "followers": 800,
        "following": 500,
        "no_profile_pic": False,
        "posts": 120,
        "default_bio": False
    },
    {
        "name": "Profile E",
        "account_age_days": 20,
        "followers": 15,
        "following": 200,
        "no_profile_pic": True,
        "posts": 4,
        "default_bio": True
    }
]


print("=" * 65)
print("       DAY 9 - FAKE PROFILE DETECTION LAB")
print("=" * 65)

for profile in profiles:

    score, risk, reasons = fake_profile_score(profile)

    print(f"\n{profile['name']}")
    print("-" * 40)
    print(f"Account age       : {profile['account_age_days']} days")
    print(f"Followers         : {profile['followers']}")
    print(f"Following         : {profile['following']}")
    print(f"Posts             : {profile['posts']}")
    print(f"No profile picture: {profile['no_profile_pic']}")
    print(f"Default bio       : {profile['default_bio']}")
    print(f"Fake score        : {score}%")
    print(f"Risk level        : {risk}")

    if reasons:
        print("Indicators:")
        for reason in reasons:
            print(f"  - {reason}")
    else:
        print("Indicators: No strong suspicious indicators")

print("\n" + "=" * 65)
print("                  ANALYSIS COMPLETE")
print("=" * 65)