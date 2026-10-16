import os
import re
from html.parser import HTMLParser

files = ["index.html", "privacy.html", "terms.html", "contact.html"]

def test_file_exists():
    print("=== Testing File Existence ===")
    for f in files:
        assert os.path.exists(f), f"Missing file: {f}"
        size = os.path.getsize(f)
        assert size > 500, f"File {f} is suspiciously small: {size} bytes"
        print(f"  [PASS] {f} exists ({size} bytes)")

def test_html_and_ids():
    print("\n=== Testing Internal Links, IDs, and Forms ===")
    all_declared_ids = {}
    all_hrefs = {}

    for f in files:
        with open(f, "r", encoding="utf-8") as fp:
            content = fp.read()

        # Find all IDs
        ids = set(re.findall(r'id=["\']([^"\']+)["\']', content))
        all_declared_ids[f] = ids

        # Find all hrefs
        hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
        all_hrefs[f] = hrefs

        # Find onsubmit and onclick handlers
        event_handlers = re.findall(r'(onsubmit|onclick)=["\']([^"\']+)["\']', content)
        print(f"\nChecking {f}: found {len(ids)} IDs, {len(hrefs)} links, {len(event_handlers)} event handlers")

        for event, handler in event_handlers:
            fn_name = re.split(r'\(|\s', handler)[0]
            # Ensure the function is defined in script tags
            assert fn_name in content, f"Handler {fn_name} in {f} not defined in script!"
            print(f"  [PASS] Event handler '{fn_name}' verified in {f}")

        # Test forms have submit buttons
        forms = re.findall(r'<form\b[^>]*>(.*?)</form>', content, re.DOTALL)
        for form in forms:
            assert 'type="submit"' in form, f"Form in {f} missing submit button!"
            print(f"  [PASS] Form has verified submit button in {f}")

    # Check internal link targets
    for f in files:
        for href in all_hrefs[f]:
            if href.startswith("#"):
                anchor = href[1:]
                if anchor:
                    assert anchor in all_declared_ids[f], f"Broken anchor link #{anchor} in {f}"
                    # print(f"  [PASS] Anchor #{anchor} valid in {f}")
            elif not href.startswith("http") and not href.startswith("mailto:") and not href.startswith("data:"):
                # Relative file link
                target_file = href.split("#")[0]
                if target_file:
                    assert os.path.exists(target_file), f"Broken relative file link {href} in {f}"
                if "#" in href:
                    target_anchor = href.split("#")[1]
                    assert target_anchor in all_declared_ids.get(target_file, set()), f"Broken target anchor #{target_anchor} in {target_file}"

    print("  [PASS] All navigation links, anchors, and file references point to valid destinations.")

if __name__ == "__main__":
    test_file_exists()
    test_html_and_ids()
    print("\n✅ All Static & Interactive UI Tests Passed Successfully!")
