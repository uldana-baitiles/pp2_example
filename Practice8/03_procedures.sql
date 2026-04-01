CREATE OR REPLACE PROCEDURE insert_or_update_user(p_username VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM contacts WHERE username = p_username
    ) THEN
        UPDATE contacts
        SET phone = p_phone
        WHERE username = p_username;
    ELSE
        INSERT INTO contacts(username, phone)
        VALUES (p_username, p_phone);
    END IF;
END;
$$;


CREATE OR REPLACE PROCEDURE insert_many_users(
    p_usernames VARCHAR[],
    p_phones VARCHAR[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1 .. array_length(p_usernames, 1)
    LOOP
        IF p_phones[i] ~ '^[0-9]{11}$' THEN
            INSERT INTO contacts(username, phone)
            VALUES (p_usernames[i], p_phones[i]);
        ELSE
            RAISE NOTICE 'Incorrect data: %, %', p_usernames[i], p_phones[i];
        END IF;
    END LOOP;
END;
$$;


CREATE OR REPLACE PROCEDURE delete_user(p_value VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM contacts
    WHERE username = p_value OR phone = p_value;
END;
$$;