# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**ScoreTune 1.0**

---

## 2. Intended Use  

This system recommends songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only — not for real users. It assumes the user knows their own taste and can describe it with a single label for genre and mood. It does not use listening history or any behavioral data.

---

## 3. How the Model Works  

Every song gets a score based on three things: genre, mood, and energy. Genre is worth 40% of the score. Mood is worth 35%. Energy is worth 25%. Genre and mood are all-or-nothing — either the song matches the user's label exactly or it gets zero for that category. Energy is different. A song closer to the user's preferred energy level scores higher, and one far away scores lower. The songs with the highest totals are returned as recommendations.

---

## 4. Data  

The catalog has 18 songs. Genres include pop, lofi, rock, jazz, hip hop, classical, country, metal, and others. Moods include happy, chill, intense, relaxed, focused, moody, and more. No songs were added or removed. Four fields in the data — tempo, valence, danceability, and acousticness — are never used in scoring. The catalog skews toward higher energy songs, which puts listeners who prefer quiet or calm music at a disadvantage.

---

## 5. Strengths  

The system works well when the user's genre and mood match something in the catalog. The Pop Fan profile (pop, happy, 0.8 energy) got a top score of 0.99 because all three fields matched a real song. The scoring logic is easy to understand. Every result shows exactly why a song was recommended, making it simple to trace a result back to the inputs. For a classroom project, that transparency is a real strength.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

When a user's preferred genre or mood does not exactly match any label in the song catalog, both the genre score and mood score are zero, leaving energy proximity as the only signal with a maximum possible score of 0.25. Despite this near-total mismatch, the system still returns a confident-looking top-five list with no warning that the recommendations are meaningless. This was confirmed by testing profiles like "hip-hop / energetic" and "classical / nostalgic," where the top results were simply whichever songs happened to have a similar energy value, not songs that matched the user's taste in any meaningful way. In a real product, this silent failure would erode user trust and push underrepresented listeners, such as fans of niche or non-English genres, toward whatever the system can rank rather than what they actually want.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

Eight user profiles were tested in total: three baselines (Pop Fan, Chill Indie, Workout Hip-Hop) and five adversarial or edge cases (Conflicting mood and energy, Nonexistent genre and mood, Zero energy, Max energy, and All-miss). For each profile the top five results were printed with their scores and explanations so it was easy to see which part of the formula was doing the work.

The most surprising result came from the Workout Hip-Hop profile. Even though "hip-hop" and "energetic" felt like a very specific, reasonable request, neither label existed in the catalog under those exact strings, so the genre and mood scores were both zero for every song. The entire top five was ranked by energy proximity alone, with max scores around 0.25, meaning the system returned a confident-looking list that was essentially sorted by tempo rather than taste.

The Conflicting profile (mood: sad, energy: 0.9) was also revealing. The expectation was that the contradiction between a sad mood and very high energy would cause unusual behavior, but the system handled it completely normally — it simply scored mood and energy as independent signals and recommended high-energy pop songs to a user who asked for sad music without any indication that the preferences were in tension.

The Zero and Max energy profiles behaved as expected at the boundaries and did not expose any bugs, which confirmed that the energy proximity formula is numerically stable across the full 0.0 to 1.0 range.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

Add a confidence score so the system can say "no good match found" instead of always returning five results. Use fuzzy matching for genre and mood so that "hip-hop" and "hip hop" are treated the same. Include acousticness and tempo in the score so more of each song's data actually matters. Add a diversity check so the top five does not repeat the same genre or artist. Allow users to provide a range for energy instead of a single value, which would better reflect how taste actually works.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

Building this made me realize how much work goes into something that looks simple. Matching a song to a user sounds straightforward, but even with just three fields the system had real blind spots. The most surprising thing was that a confident-looking result does not mean the system actually understood what the user wanted. A score of 0.23 and a score of 0.99 look identical in the output, which felt wrong once I saw it. Now when I use Spotify or YouTube I think about what signals they are actually using and what they might be quietly ignoring. A recommendation is not proof that the system knows you — it is just the best guess it could make with the data it had.

If I extended this project, the first thing I would fix is the confidence problem. I would add a minimum score threshold so the system says "no strong match found" instead of returning noise. After that I would bring in the unused fields — acousticness and tempo especially — because those feel like they actually shape whether a song fits a moment. I would also try letting the user rate a few results and use that feedback to adjust the weights over time, which is closer to how real recommenders learn. Finally I would test it on a much larger catalog to see if the exact-match problem with genre and mood gets worse at scale or if more data naturally covers more label variations.
