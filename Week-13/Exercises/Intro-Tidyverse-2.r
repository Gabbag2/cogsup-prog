
data <- read_csv(
  "C:/Users/gabri/Desktop/exp approach/prof/PPE/Week-13/Exercises/data/148338_220209_095045_M057814.csv",
  skip = 2
)

education_level <- data %>% pull(response) %>% first()  

data <- data %>%
  # Keep only useful columns
  select(c(rowNo, type, stim1, stim2, stimPos, trialType, response, RT)) %>%
  
  # Keep only useful rows
  filter(type != "form") %>%
  
  # Add demographic and trial-number info, turn trial type to factor
  mutate(
    education_level = education_level, # Add info
    trial_number = row_number(),
    trialType = factor(trialType, levels = c("incongruent", "congruent"))
  ) %>%
  
  # Rename trialType to trial_type
  rename(trial_type = trialType)

data2 <- select(data, -rowNo  , -type)
data <- rename(data, stim_left = stim1, stim_right = stim2)
data <- data %>%
  mutate(
    correct_side = case_when(
      str_detect(stim_left,  "Small") ~ "left",
      str_detect(stim_right, "Small") ~ "right",
      TRUE ~ NA_character_
    )
  )
head(data)

data$subject_id <- 1
head(data)
data$correct_key <- ifelse(data$correct_side == "left", "f",
                           ifelse(data$correct_side == "right", "j", NA))
data$correct <- ifelse(data$response == data$correct_key, 1, 0)
data$trial_block <- ifelse(data$trial_number <= 120, 1, 2)
data$trial_number <- ((data$trial_number - 1) %% 120) + 1

#10
data <- data %>%
  select(subject_id, education_level, trial_block, trial_number, everything())
head(data)

#11
library(tidyverse)

raw_data <- read_csv(
  "C:/Users/gabri/Desktop/exp approach/prof/PPE/Week-13/Exercises/data/148338_220209_095045_M057814.csv",
  skip = 2
)

tidy_data <- raw_data %>%
  
  select(rowNo, type, stim1, stim2, stimPos, trialType, response, RT) %>%
  
  filter(type != "form") %>%
  
  mutate(
    subject_id = 1,
    education_level = first(response),     # récupère la réponse du formulaire (1ère ligne)
    trial_number = row_number()
  ) %>%
  
  mutate(
    trialType = factor(trialType, levels = c("incongruent", "congruent"))
  ) %>%
  rename(
    trial_type = trialType,
    stim_left  = stim1,
    stim_right = stim2,
    stim_pos   = stimPos,
    rt         = RT
  ) %>%
  
  mutate(
    correct_side = case_when(
      str_detect(stim_left,  "Small") ~ "left",
      str_detect(stim_right, "Small") ~ "right",
      TRUE ~ NA_character_
    )
  ) %>%
  
  mutate(
    correct_key = ifelse(correct_side == "left", "f",
                         ifelse(correct_side == "right", "j", NA_character_))
  ) %>%
  
  mutate(
    correct = ifelse(as.character(response) == correct_key, 1, 0)
  ) %>%
  
  mutate(
    trial_block = ifelse(trial_number <= 120, 1, 2),
    trial_number = ((trial_number - 1) %% 120) + 1
  ) %>%
  
  select(subject_id, education_level, trial_block, trial_number, everything())
  

head(tidy_data)
colnames(tidy_data)

#12 
tidy_data %>%
  summarize(
    mean_rt = mean(rt, na.rm = TRUE),
    error_rate = mean(1 - correct, na.rm = TRUE),
    .by = trial_type
  )

#13
tidy_data %>%
  summarize(
    mean_rt = mean(rt, na.rm = TRUE),
    error_rate = mean(1 - correct, na.rm = TRUE),
    .by = correct_side
  )

#14
tidy_data %>%
  summarize(
    mean_rt = mean(rt, na.rm = TRUE),
    error_rate = mean(1 - correct, na.rm = TRUE),
    .by = c(trial_type, correct_side)
  )

head(tidy_data)

#15
files <- list.files(
  path = "C:/Users/gabri/Desktop/exp approach/prof/PPE/Week-13/Exercises/data",
  pattern = "\\.csv$",
  full.names = TRUE
)

raw_data <- map_dfr(files, read_csv, skip = 2, col_types = cols(), .id = "id")


tidy_data <- raw_data %>%
  select(rowNo, type, stim1, stim2, stimPos, trialType, response, RT, id) %>%
  filter(type != "form") %>%
  
 
  group_by(id) %>%
  mutate(education_level = first(response)) %>%
  ungroup() %>%
  
  mutate(
    trial_number = row_number(), 
    trialType = factor(trialType, levels = c("incongruent", "congruent"))
  ) %>%
  
  rename(
    trial_type = trialType,
    stim_left  = stim1,
    stim_right = stim2,
    stim_pos   = stimPos,
    rt         = RT
  ) %>%
  
  group_by(id) %>%
  mutate(
    trial_number = row_number(),
    correct_side = case_when(
      str_detect(stim_left,  "Small") ~ "left",
      str_detect(stim_right, "Small") ~ "right",
      TRUE ~ NA_character_
    ),
    correct_key = ifelse(correct_side == "left", "f",
                         ifelse(correct_side == "right", "j", NA_character_)),
    correct = ifelse(as.character(response) == correct_key, 1, 0),
    trial_block = ifelse(trial_number <= 120, 1, 2),
    trial_number = ((trial_number - 1) %% 120) + 1
  ) %>%
  ungroup() %>%
  
  select(id, education_level, trial_block, trial_number, everything())

head(tidy_data)


#16
n_before <- nrow(tidy_data)

tidy_data <- tidy_data %>%
  filter(rt >= 200, rt <= 1500)

n_excluded_trials <- n_before - nrow(tidy_data)
n_excluded_trials

#17
acc_by_subj <- tidy_data %>%
  summarize(accuracy = mean(correct, na.rm = TRUE), .by = id)

excluded_ids <- acc_by_subj %>%
  filter(accuracy < 0.93) %>%
  pull(id)

n_excluded_subjects <- length(excluded_ids)
n_excluded_subjects

tidy_data <- tidy_data %>%
  filter(!(id %in% excluded_ids))

#18
stroop_summary <- tidy_data %>%
  summarize(
    mean_rt   = mean(rt, na.rm = TRUE),
    accuracy  = mean(correct, na.rm = TRUE),
    error_rate = mean(1 - correct, na.rm = TRUE),
    n = dplyr::n(),
    .by = trial_type
  )

stroop_summary


