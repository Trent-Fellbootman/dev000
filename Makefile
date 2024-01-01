SOURCEDIR := docs/en
LANGUAGES := zh ru ja # Add more languages as needed

# Function to generate a list of target files for a language
define generate_targets
$(subst $(SOURCEDIR),docs/$(1),$(shell find $(SOURCEDIR) -type f))
endef

# Generate rules for each language
define generate_rules
docs/$(1)/%.md: $(SOURCEDIR)/%.md
	@mkdir -p $$(@D)
	@echo "Translating Markdown file $$< to $$@ for language $(1)..."
	@scripts/ai_translate.py $(1) $$< $$@

docs/$(1)/%: $(SOURCEDIR)/%
	@mkdir -p $$(@D)
	@echo "Copying file $$< to $$@ for language $(1)..."
	@cp $$< $$@
endef

# Default target for all languages
translate: $(foreach lang,$(LANGUAGES),translate-$(lang))

# Define a translate target for each language
$(foreach lang,$(LANGUAGES),\
$(eval translate-$(lang): $$(call generate_targets,$(lang)))\
)

# Generate rules for all languages
$(foreach lang,$(LANGUAGES),$(eval $(call generate_rules,$(lang))))

.PHONY: translate $(foreach lang,$(LANGUAGES),translate-$(lang))
