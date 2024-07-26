var flagArea = document.getElementById("flags");
flagArea.onchange = updateComponents;
var seedInput = document.getElementById("seed");
seedInput.onchange = updateFlags;
var attackGrid = document.getElementById("attack-grid");
var throwGrid = document.getElementById("throw-grid");
var attributeGrid = document.getElementById("attribute-grid");
var geckoGrid = document.getElementById("gecko-grid");
var etcGrid = document.getElementById("etc-grid");
var grids = [attackGrid, throwGrid, attributeGrid, geckoGrid, etcGrid];
var flagInput = document.getElementById("entry");
var entries = [];
var geckoEntries = [];
var options = document.getElementsByClassName("menu-options");
var flagNames = [];
var lastFlagset = "";
var customFlags = "";

function addFlagEntry(grid, entryName, flagName, tooltip="", _entries=entries) {
    newEntry = flagInput.cloneNode(true);
    let checkbox = newEntry.children[0];
    let label = newEntry.children[1];
    let selection = newEntry.children[2];
    if (_entries == geckoEntries) {
        selection.remove();
        label.style.width = "90%";
        checkbox.checked = false;
    }
    label = newEntry.children[1];
    label.innerHTML = entryName;
    label.onmousedown = function () {
        if (checkbox.checked) {
            checkbox.checked = false;
        } else {
            checkbox.checked = true;
        }
        updateFlags();
    }
    newEntry.getvalue = entryName;
    newEntry.data = flagName;
    flagNames.push(flagName);
    newEntry.id = newEntry.id + entries.length;
    newEntry.style.display = "block";
    newEntry.onchange = updateFlags;
    addTooltip(newEntry, tooltip);
    _entries.push(newEntry);
    grid.appendChild(newEntry);
    updateFlags();
}

function updateFlags() {
    flagset = ""
    if (seedInput.value.length > 0) {
        flagset += "-seed " + seedInput.value + " ";
    }
    flagArea.value = flagset;
    for (let i = 0; i < entries.length; i++) {
        if (entries[i].children[0].checked) {
            flagset += entries[i].data + " " + (entries[i].children[2].selectedIndex + 1) + " ";
        }
    }
    for (let i = 0; i < geckoEntries.length; i++) {
        if (geckoEntries[i].children[0].checked) {
            flagset += geckoEntries[i].data + " ";
        }
    }
    flagset += customFlags;
    flagArea.value = flagset;
    lastFlagset = flagset;
};

function updateComponents() {
    flagset = flagArea.value + "-";
    if (flagset.includes("-seed")) {
        seedInput.value = getStringAfter(flagset, "-seed");
    }
    allFlags = entries.concat(geckoEntries);
    for (let i = 0; i < flagNames.length; i++) {
        if (flagset.includes(flagNames[i])) {
            allFlags[i].children[0].checked = true;
            flagParameter = getStringAfter(flagset, flagNames[i]);
            if (allFlags[i].children.length > 2) {
                allFlags[i].children[2].selectedIndex = (flagParameter - 1);
            }
        } else {
            allFlags[i].children[0].checked = false;
        }
    }
    flagset = flagset.substring(0, flagset.length - 1);
    var newCustomFlags = flagset.replace(lastFlagset, "")
    customFlags += newCustomFlags;
}

function getStringAfter(string, start) {
    new_string = string.split(start).pop().split(/-|\&/)[0];
    new_string = new_string.replace(" ", "")
    return new_string
}

addFlagEntry(attackGrid, "Damage", "&attack_damage", "Modifies the amount of damage (percent) attacks do.");
addFlagEntry(attackGrid, "Angle", "&attack_angle", "Modifies the angle at which attacks send.");
addFlagEntry(attackGrid, "Knockback Growth", "&attack_growth", "This value controls the rate at which percentage affects knockback.");
addFlagEntry(attackGrid, "Set Knockback", "&attack_setkb", "Randomizes attacks which send at a fixed knockback, like Shine. Enabling this option gives a chance for new attacks to have this property.");
addFlagEntry(attackGrid, "Base Knockback", "&attack_base", "The minimum knockback an attack will have.");
addFlagEntry(attackGrid, "Elements", "&attack_element", "Can add elements like fire to attacks. Lower chance for elements that restrict movement.");
addFlagEntry(attackGrid, "SFX", "&attack_sfx", "Changes the sound effect when a move lands.");
addFlagEntry(attackGrid, "Hitbox Size", "&attack_size", "Changes the size of an attack's hitboxes.");
addFlagEntry(throwGrid, "Damage", "&throw_damage", "Modifies the amount of damage (percent) throws do.");
addFlagEntry(throwGrid, "Angle", "&throw_angle", "Modifies the angle at which throws send.");
addFlagEntry(throwGrid, "Knockback Growth", "&throw_growth", "This value controls the rate at which percentage affects knockback.");
addFlagEntry(throwGrid, "Set Knockback", "&throw_setkb", "Randomizes throws which send at a fixed knockback. Has a chance to give throws this property.");
addFlagEntry(throwGrid, "Base Knockback", "&throw_base", "The minimum knockback a throw will have");
addFlagEntry(throwGrid, "Elements", "&throw_element", "Can add random elements to throws, but they are just for aesthetics.");
addFlagEntry(attributeGrid, "Normal Attributes", "&attributes", "Affects values shared by all fighters that control the way they move or other values such as the size or frames of attack after an L cancel.");
addFlagEntry(attributeGrid, "Special Attributes", "&special_attributes", "Affects values unique to each fighter that are related to their special moves, projectiles, etc.");
addFlagEntry(geckoGrid, "Air Dodge Item Catch", "-gecko_air_dodge_catch", "Credit: Uncle Punch | Air dodging into projectiles that can be caught will catch them, similar to future Smash Brothers games.", geckoEntries);
addFlagEntry(geckoGrid, "Air Grab", "-gecko_air_grab", "Credit: Uncle Punch | Allows for grab to be performed while airborne.", geckoEntries);
addFlagEntry(geckoGrid, "Paper Mode", "-gecko_paper_mode", "Credit: DRGN | All fighter will be flat like Game and Watch (no Z-Axis).", geckoEntries);
addFlagEntry(geckoGrid, "All Fighters Float", "-gecko_all_float", "Credit: Uncle Punch | Every fighter can perform a float the same way Peach can.", geckoEntries);
addFlagEntry(geckoGrid, "Auto L Cancel", "-gecko_auto_lcancel", "Credit: Dan Salvato | L Cancels are performed automatically.", geckoEntries);
addFlagEntry(geckoGrid, "B Reverse", "-gecko_breverse", "Credit: Uncle Punch | Neutral B moves can be reversed by quickly moving the control stick in the opposite direction before pressing B.", geckoEntries);
addFlagEntry(geckoGrid, "Bowser Flame Cancel", "-gecko_flame_cancel", "Credit: Achilles | Bowser's flame attack can be cancelled by landing on the ground, similar to Falco's laser.", geckoEntries);
addFlagEntry(geckoGrid, "L to Brawl Airdodge", "-gecko_brawl_airdodge", "Credit: Uncle Punch | Pressing L results in an airdodge similar to how it works in Super Smash Bros. Brawl.", geckoEntries);
addFlagEntry(geckoGrid, "All Fighters Walljump", "-gecko_all_walljump", "Credit: Achilles, Geuse | All fighters are able to perform a walljump similar to how characters like Fox or Mario are able to.", geckoEntries);
addFlagEntry(geckoGrid, "Fastfall Whenever", "-gecko_fastfall_whenever", "Credit: Uncle Punch | All fighters are able to fastfall before reaching the peak of their jump.", geckoEntries);
addFlagEntry(geckoGrid, "No Meteor Cancel", "-gecko_no_meteor", "Credit: flieskiller | Players will no longer be able to meteor cancel attacks that send straight down.", geckoEntries);
addFlagEntry(geckoGrid, "No Shield", "-gecko_no_shield", "Credit: Achilles | Characters will be unable to use their shield.", geckoEntries);
addFlagEntry(geckoGrid, "Perfect Shield", "-gecko_perfect_shield", "Credit: Uncle Punch | Releasing the shield button with proper timing creates an opening for counter attack, similar to in Super Smash Bros. Ultimate.", geckoEntries);
addFlagEntry(geckoGrid, "Reverse Aerial Rush", "-gecko_rar", "Credit: MagicScrumpy | Fighters can turn around a split second before performing an aerial attack.", geckoEntries);
addFlagEntry(geckoGrid, "Shadow Mode", "-gecko_shadow_mode", "Credit: ??? | All characters will have their models replaced with a variant that is completely black.", geckoEntries);
addFlagEntry(geckoGrid, "Super Shine Bros.", "-gecko_shine_bros", "Credit: Uncle Punch | All characters will have their down special replaced with Shine.", geckoEntries);

// MENU CODE
attackRadio = document.getElementById("attack-menu");
throwRadio = document.getElementById("throw-menu");
attributeRadio = document.getElementById("attribute-menu");
geckoRadio = document.getElementById("gecko-menu");
etcRadio = document.getElementById("etc-menu");

radios = document.querySelectorAll("input[type=radio]");
options[0].style.backgroundColor = "gold";
options[0].children[1].style.color = "blue";

function disableAll() {
    for (let i = 0; i < grids.length; i++) {
        grids[i].style.display = "none";
    }
}

function resetOptionColors() {
    for (let i = 0; i < options.length; i++) {
        options[i].style.backgroundColor = "#4400BB44";
        options[i].children[1].style.color = "silver";
    }
}

for (let i = 0; i < radios.length; i++) {
    radios[i].onchange = function() {
        disableAll();
        resetOptionColors();
        if (radios[i].checked) {
            grids[i].style.display = "grid";
            options[i].style.backgroundColor = "gold";
            options[i].children[1].style.color = "blue";
        }
    }

}

for (let i = 0; i < options.length; i++) {
    options[i].onmouseover = function() {
        if (!radios[i].checked) {
            options[i].style.backgroundColor = "#8800BBA0";
        }
    }
    options[i].onmouseout = function() {
        if (!radios[i].checked) {
            options[i].style.backgroundColor = "#4400BB44";
        }
    }
}

// TOOLTIPS
tooltipDisplay = document.getElementById("tooltips");

function addTooltip(object, message) {
    object.onmouseover = function() {
        tooltipDisplay.innerHTML = message;
    }
} 

