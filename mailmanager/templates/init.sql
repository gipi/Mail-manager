--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'SQL_ASCII';
SET standard_conforming_strings = off;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET escape_string_warning = off;

SET search_path = public, pg_catalog;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('users_id_seq', 5, true);


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: users; Type: TABLE; Schema: public; Owner: mailuser; Tablespace: 
--
CREATE TABLE users (
    userid character varying(128) NOT NULL,
    domain character varying(128) NOT NULL,
    password character varying(64) NOT NULL,
    home character varying(255) NOT NULL,
    uid integer NOT NULL,
    gid integer NOT NULL,
    id integer DEFAULT nextval('users_id_seq'::regclass) NOT NULL
);


ALTER TABLE public.users OWNER TO mailuser;

--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: mailuser
--

COPY users (userid, domain, password, home, uid, gid, id) FROM stdin;
test    example.com     yMAq2mkG/JG8MFoU10vawpUHQQj5HglWlQoQzBaLU8IQcQnP        example.com/test/       8       8       3
testbis example.com     tEoDe9rt6PgJ9xFkDK9f90r/W7i46M8GenGpdoSZH/I5gVEy        example.com/testbis/    8       8       4
miao    example.com     DykyZ9HtDNPSJIGCK2lh21uHXlcwQc+ND05JalZhOF5mOWhJMGlaNA==        miao/example.com        8       8       5
\.


--
-- Name: users_pkey; Type: CONSTRAINT; Schema: public; Owner: mailuser; Tablespace: 
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- Name: users_id_seq; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON SEQUENCE users_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE users_id_seq FROM postgres;
GRANT ALL ON SEQUENCE users_id_seq TO postgres;
GRANT ALL ON SEQUENCE users_id_seq TO mailuser;

--
-- Name: users; Type: ACL; Schema: public; Owner: mailuser
--

REVOKE ALL ON TABLE users FROM PUBLIC;
REVOKE ALL ON TABLE users FROM mailuser;
GRANT ALL ON TABLE users TO mailuser;


--
-- PostgreSQL database dump complete
--
