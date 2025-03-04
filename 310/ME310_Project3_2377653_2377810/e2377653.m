clear 
clc

f = fopen("input.txt");
data = textscan(f,'%s');
fclose(f);
variable = str2double(data{1}(1:1:end));

[j] = size(variable);

xx = variable(1:1:j/2);
yy = variable(j/2+1:1:end);

nn = length(xx);

A = zeros(5*(nn-1),5*(nn-1));
b = zeros(5*(nn-1),1);

%xx = [1 1.1 2 2.3 3 4 4.5 5 5.5 6 7];
%yy = [-0.1585 -0.1088 -0.0907 ...
%    -0.2543 -0.8589 -1.7568 ...
%    -1.9775 -1.9589 -1.7055 ...
%    -1.2794 -0.3430];

for di1 = 1:nn-1
    A(di1,(di1-1)*5+1) = 1;
    A(di1+(nn-1), (di1-1)*5+(1:5)) = [1 ...
        (xx(di1+1)-xx(di1)) ...
        (xx(di1+1)-xx(di1))^2 ...
        (xx(di1+1)-xx(di1))^3 ...
        (xx(di1+1)-xx(di1))^4 ];
    b(di1) = yy(di1);
    b(di1 + (nn-1)) = yy(di1+1);
end 

for di1 = 1:nn-2
    A(di1+(nn-1)*2,(di1-1)*5+(1:5)) = [0 ...
        1 ...
        2*(xx(di1+1)-xx(di1)) ...
        3*(xx(di1+1)-xx(di1))^2 ...
        4*(xx(di1+1)-xx(di1))^3];
    A(di1+(nn-1)*2,(di1+1-1)*5+(1:5)) = [0 ...
        -1 ...
        0 ...
        0 ...
        0 ];
end 

for di1 = 1:nn-2
    A(di1+(nn-1)*3-1,(di1-1)*5+(1:5)) = [0 ...
        0 ...
        2 ...
        6*(xx(di1+1)-xx(di1)) ...
        12*(xx(di1+1)-xx(di1))^2 ];
    A(di1+(nn-1)*3-1,(di1+1-1)*5+(1:5)) = [0 ...
        0 ...
        -2 ...
        0 ...
        0 ];
end 

for di1 = 1:nn-2
    A(di1 +(nn-1)*4-2,(di1-1)*5+(1:5)) = [0 ...
        0 ...
        0 ...
        6 ...
        24*(xx(di1+1)-xx(di1)) ];
    A(di1 +(nn-1)*4-2,(di1+1-1)*5+(1:5)) = [0 ...
        0 ...
        0 ...
        -6 ...
        0 ];    
end 

A(5*(nn-1)-2,3) = 1;
A(5*(nn-1)-1,4) = 1;
A(5*(nn-1),5*(nn-1)) = 1;

S = A\b;

figure
title('Quadratic Spline')
xlabel('x inputs') 
ylabel('y outputs') 
hold on 
for di1 = 1:(nn-1)
    xnow = linspace(xx(di1),xx(di1+1),(nn-1));
    ynow = zeros(size(xnow)) ;
    for di2 = 1:length(xnow)
        ynow(di2) = transpose(S((di1-1)*5+(1:5)))* ...
            [1; ...
            (xnow(di2)-xnow(1)); ...
            (xnow(di2)-xnow(1))^2; ...
            (xnow(di2)-xnow(1))^3; ...
            (xnow(di2)-xnow(1))^4 ];
    end
    plot(xnow,ynow)
end 

figure
title('Quadratic Spline First Derivatives')
xlabel('x inputs') 
ylabel('y outputs') 
hold on 
for di1 = 1:(nn-1)
    xnow = linspace(xx(di1),xx(di1+1),(nn-1));
    ynow = zeros(size(xnow)) ;
    for di2 = 1:length(xnow)
        ynow(di2) = transpose(S((di1-1)*5+(1:5)))* ...
            [0; ...
            1; ...
            2*(xnow(di2)-xnow(1)); ...
            3*(xnow(di2)-xnow(1))^2; ...
            4*(xnow(di2)-xnow(1))^3 ];
    end
    plot(xnow,ynow)
end 

x_input = input('enter the x input: ');
y_output = 0;

if x_input<xx(1) || x_input>xx(nn)
    fprintf('input is out of the interval')
end 

for t = 1:(nn)
    if  x_input>=xx(t) && x_input<=xx(t+1)
        y_output =  transpose(S((t-1)*5+(1:5)))* ...
            [1; ...
            (x_input-xx(t)); ...
            (x_input-xx(t))^2; ...
            (x_input-xx(t))^3; ...
            (x_input-xx(t))^4 ];
    break 
    end
end 
fprintf('the y outout is: %.4f\n', y_output)