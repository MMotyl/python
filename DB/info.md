CREATE LOGIN python 
    WITH PASSWORD = 'Python2022';  
GO  
create user python for login python;
GO
ALTER ROLE db_owner
	ADD MEMBER python;  
GO