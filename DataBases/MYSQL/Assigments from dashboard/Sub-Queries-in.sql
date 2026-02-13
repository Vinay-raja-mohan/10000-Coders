-- Active: 1767583816891@@127.0.0.1@3306@assignments
CREATE TABLE Insta_post (
    post_id INT PRIMARY KEY,
    user_id INT,
    username VARCHAR(50),
    caption VARCHAR(255),
    likes INT,
    comments INT,
    created_at DATE
);

INSERT INTO Insta_post VALUES
(101, 1, 'yash_123', 'Morning vibes 🌞', 120, 15, '2023-01-01'),
(102, 2, 'neha_insta', 'Travel diaries ✈️', 300, 40, '2023-02-10'),
(103, 3, 'raj_cool', 'My new painting 🎨', 95, 10, '2023-02-20'),
(104, 1, 'yash_123', 'Happy Holi! 🌈', 500, 80, '2023-03-08'),
(105, 4, 'anita_star', 'Workout motivation 💪', 250, 25, '2023-03-15'),
(106, 5, 'vikas_travel', 'Beautiful sunset 🌅', 400, 60, '2023-03-20'),
(107, 3, 'raj_cool', 'Foodie life 🍕', 150, 20, '2023-04-05'),
(108, 2, 'neha_insta', 'Best friends ❤️', 600, 100, '2023-04-12'),
(109, 5, 'vikas_travel', 'Mountain trek 🏔️', 550, 90, '2023-04-25'),
(110, 4, 'anita_star', 'Self care Sunday 🧘‍♀️', 200, 18, '2023-05-01');

select * from insta_post;


-- 1. Find posts with likes greater than the average likes of all posts.
select * from insta_post where likes >
(select avg(likes) from insta_post);

-- 2. Find posts that have more comments than the average comments of all posts.
select * from insta_post where comments >
(select avg(comments) from insta_post);

-- 3. Find the post(s) with the maximum likes.
select * from insta_post where likes =
(select max(likes) from insta_post);

-- 4. Find the post(s) with the minimum likes.
select * from insta_post where likes =
(select min(likes) from insta_post);

-- 5. Find the caption of the second most liked post.
select caption from insta_post where likes =
(select max(likes) from insta_post where likes <
(select max(likes) from insta_post));

-- 6. Find posts created on the same date as the most liked post.
select * from insta_post where created_at = 
(select created_at from insta_post where likes = 
(select max(likes) from insta_post));

-- 7. Find posts with likes greater than twice the likes of post_id = 103.

(select * from insta_post where likes > 
(select likes from insta_post where post_id=103)*2);

-- 8. Find posts made before the earliest post date.
select * from insta_post where created_at <
(select min(created_at) from insta_post);

-- 9. Find posts made after the latest post date.
select * from insta_post where created_at >
(select max(created_at) from insta_post);

-- 10. Find posts that have comments equal to the maximum comments.
select * from insta_post where comments =
(select max(comments) from insta_post);
