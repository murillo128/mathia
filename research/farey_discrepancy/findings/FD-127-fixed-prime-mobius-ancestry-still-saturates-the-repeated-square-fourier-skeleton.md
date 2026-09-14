# FD-127 — fixed-prime Möbius ancestry still saturates the repeated-square Fourier skeleton

**Status:** `EXACT-DERIVED + FLOOR-QUOTIENT-FOURIER-SKELETON + HORIZON-INDEPENDENT-SQUAREFREE-SIGNS + FIXED-PRIME-MOBIUS-ANCESTRY + SQUARE-ROOT-ENVELOPE + REPEATED-SQUARE-SATURATION + NEGATIVE/ROUTE-RESTRICTION`.

`FD-126` leaves the actual organization of the squarefree signs as the first unpriced source information. The weakest genuinely multiplicative test is to force the true Möbius sign rule in a fixed finite set of prime directions. That still does not create a critical gap on the minimal floor-quotient Fourier skeleton.

Fix a finite set of primes `P` and write

\[
Q:=\prod_{p\in P}p.
\tag{1}
\]

There are an integer `H_0` and one infinite sequence `a` such that

\[
a(1)=1,\qquad
a(n)=0\quad(n\text{ nonsquarefree}),\qquad
a(n)\in\{-1,+1\}\quad(n\text{ squarefree}),
\tag{2}
\]

and, simultaneously for every `p in P`,

\[
\boxed{
a(pn)=-a(n)\qquad(p\nmid n).
}
\tag{3}
\]

Let

\[
Y(x):=\sum_{n\le x}a(n).
\tag{4}
\]

The source can be chosen with the global critical envelope

\[
\boxed{|Y(n)|\ll_P\sqrt n.}
\tag{5}
\]

For the repeated-square chain

\[
H_{j+1}=H_j^2,
\tag{6}
\]

let

\[
\mathcal Q_H
:=
\left\{\left\lfloor\frac Hm\right\rfloor:1\le m\le H\right\},
\qquad
\tau_H(k):=\left\lfloor\frac Hk\right\rfloor,
\tag{7}
\]

and retain the `FD-118` Fourier skeleton

\[
A_H(k):=\sum_{d\mid k}d\,Y(\tau_H(d)),
\qquad
\mathcal E_H^{\mathcal Q}(Y)
:=
\sum_{k\in\mathcal Q_H}\frac{|A_H(k)|^2}{k^2}.
\tag{8}
\]

At every retained horizon there is an integer `t_j` with the forced squarefree parity and

\[
|t_j-\sqrt{H_j}|\le1,\qquad Y(H_j)=t_j,
\tag{9}
\]

such that

\[
\boxed{
\mathcal E_{H_j}^{\mathcal Q}(Y)
=
t_j^2
+
O_P\!\left(H_j^{3/4}(\log H_j)^2\right).
}
\tag{10}
\]

Consequently

\[
\boxed{
\frac{\mathcal E_{H_j}^{\mathcal Q}(Y)}{|Y(H_j)|^2}
=
1+O_P\!\left(H_j^{-1/4}(\log H_j)^2\right)
\longrightarrow1.
}
\tag{11}
\]

Thus **any fixed finite amount of exact prime-by-prime Möbius ancestry is still insufficient**. The source in `FD-126` can be upgraded from arbitrary squarefree unit signs to a sequence obeying the true Möbius multiplicative rule in every direction from an arbitrary fixed finite prime set, without losing the common-source property, the square-root envelope, or repeated-square saturation. A coercive theorem must therefore spend prime breadth growing with scale, full/global multiplicativity, a growing divisor/cross-horizon identity family, or another genuinely non-finite sign-correlation law.

## 1. Factor the prescribed prime directions out of the free signs

Use the same finite-prime factorization as `FD-027`. Define the squarefree `P`-free core

\[
\mathcal C_P
:=
\{m\ge1:m\text{ squarefree and }(m,Q)=1\}.
\tag{12}
\]

Choose signs `b_m in {-1,+1}` on `\mathcal C_P`, with `b_1=1`, and put

\[
B(x):=\sum_{\substack{m\le x\\m\in\mathcal C_P}}b_m.
\tag{13}
\]

Every squarefree integer has a unique representation

\[
n=q\,m,\qquad q\mid Q,\quad m\in\mathcal C_P.
\tag{14}
\]

Define

\[
a(n)=
\begin{cases}
\mu(q)b_m,&n=qm\text{ as in (14)},\\
0,&n\text{ nonsquarefree}.
\end{cases}
\tag{15}
\]

Then (2) is automatic, and multiplying by a prime `p in P` not already dividing `n` toggles exactly one factor in `q`, proving (3). Summing (15) over `q` gives the exact source relation

\[
\boxed{
Y(x)
=
\sum_{q\mid Q}\mu(q)\,
B\!\left(\left\lfloor\frac{x}{q}\right\rfloor\right).
}
\tag{16}
\]

For `q_d=floor(H/d)`, nested floors give

\[
\boxed{
Y(q_d)
=
\sum_{q\mid Q}\mu(q)\,B(q_{qd}).
}
\tag{17}
\]

The number of available core positions satisfies the elementary finite-prime squarefree count

\[
\mathsf Q_P(x)
:=
\#\{m\le x:m\in\mathcal C_P\}
=
c_Px+O_P(\sqrt x),
\qquad
c_P
=
\frac1{\zeta(2)}
\prod_{p\in P}\frac{p}{p+1}>0.
\tag{18}
\]

Hence, after choosing the window constant large enough depending on `P`, every interval of length `C_P sqrt(x)` near a sufficiently large `x` contains `gg_P sqrt(x)` legal core positions. This is the only local supply input.

## 2. A finite triangular inversion realizes the equality prefix

Suppose the core signs are already fixed through `L=H_{j-1}` and set

\[
H=L^2,\qquad
R=\lfloor H^{1/4}\rfloor,\qquad
q_d=\left\lfloor\frac Hd\right\rfloor.
\tag{19}
\]

Because `Q` is fixed,

\[
q_{QR+1}\asymp_P H^{3/4}\gg L,
\tag{20}
\]

so all endpoint interpolation below occurs in fresh source territory.

Choose `t` to be the integer of the forced squarefree parity nearest `sqrt(H)`. For `1<=d<=R`, choose an integer `y_d` with

\[
y_1=t,\qquad
y_d\equiv \#\{n\le q_d:n\text{ squarefree}\}\pmod2,
\qquad
\left|y_d-t\frac{\mu(d)}d\right|\le1.
\tag{21}
\]

Write

\[
z_d:=B(q_d).
\tag{22}
\]

For the boundary range `R<d<=QR`, choose `z_d in {0,1}` with the forced core parity

\[
z_d\equiv\mathsf Q_P(q_d)\pmod2.
\tag{23}
\]

Then define `z_d` for `d=R,R-1,...,1` by

\[
\boxed{
z_d
=
y_d
-
\sum_{\substack{q\mid Q\\q>1}}
\mu(q)z_{qd}.
}
\tag{24}
\]

Every index on the right is larger than `d` and at most `QR`, so the recurrence is well-defined. By (17),

\[
\boxed{Y(q_d)=y_d\qquad(1\le d\le R).}
\tag{25}
\]

Parity also closes exactly. Unique factorization (14) gives

\[
\#\{n\le x:n\text{ squarefree}\}
=
\sum_{q\mid Q}
\mathsf Q_P\!\left(\left\lfloor\frac{x}{q}\right\rfloor\right).
\tag{26}
\]

Since every `mu(q)` for `q|Q` is odd modulo `2`, descending induction in (24), using (21), (23), and (26), yields

\[
\boxed{
z_d\equiv\mathsf Q_P(q_d)\pmod2
\qquad(1\le d\le QR).
}
\tag{27}
\]

Thus every prescribed endpoint is realizable by actual `+-1` core signs.

The size of the inverse is harmless because `P` is fixed. With `(T_pz)_d=z_{pd}`, the operator in (17) is `prod_(p in P)(I-T_p)`. As in `FD-027`,

\[
\prod_{p\in P}(I-T_p)^{-1}
=
\sum_{s\in\langle P\rangle}T_s,
\qquad
\sum_{s\in\langle P\rangle}\frac1s
=
\prod_{p\in P}(1-p^{-1})^{-1}<\infty.
\tag{28}
\]

Using (21) and the `0/1` boundary therefore gives

\[
\boxed{
|z_d|
\ll_P
\frac{\sqrt H}{d}
+
(1+\log R)^{|P|}
\qquad(d\le R),
}
\tag{29}
\]

while `|z_d|<=1` for `R<d<=QR`.

## 3. The permanent core walk can realize all endpoints at square-root cost

Let

\[
I_d=(q_{d+1},q_d]\cap\mathbb Z.
\tag{30}
\]

Uniformly for `d<=QR`,

\[
|I_d|\asymp\frac{H}{d^2},
\qquad
\frac{|I_d|}{\sqrt{H/d}}
\asymp
\frac{\sqrt H}{d^{3/2}}
\gg_P H^{1/8}.
\tag{31}
\]

The core-count estimate (18) therefore supplies many more legal positions in each `I_d` than are needed to realize the endpoint change in (29). Starting above `L`, first use a `O_P(sqrt(L))` window to drive the inherited core sum to absolute value at most `1`; then alternate unused core signs until the first prescribed endpoint. In each `I_d`, use a lower square-root window to reduce the current value to `O(1)`, alternate through the middle, and use an upper square-root window to reach the exact `z_d`.

The endpoint bound (29) is compatible with those windows because

\[
\frac{\sqrt H}{d}
\le
\sqrt{\frac Hd},
\tag{32}
\]

and the polylogarithmic term is smaller than `sqrt(H/d)` uniformly for `d<=R` once `H` is large. Thus the signs can be assigned without changing any old prefix.

The construction gives

\[
|B(n)|\ll_P\sqrt n
\tag{33}
\]

globally. Equation (16) then yields (5). It also preserves the induction bound

\[
\sum_{n\le H}|B(n)|^2\ll_P H^{3/2}.
\tag{34}
\]

Indeed the ramp in `I_d` has length `O_P(sqrt(H/d))` and height `O_P(sqrt(H)/d+polylog(H))`, so the leading squared cost is

\[
O_P\!\left(\frac{H^{3/2}}{d^{5/2}}\right),
\tag{35}
\]

which is summable in `d`; all middle regions are bounded.

More importantly, if

\[
X:=q_{R+1}\asymp H^{3/4},
\tag{36}
\]

then the high-amplitude ramps `d<=R` lie above `X`. Below `X`, the new core walk is bounded except for the initial reset, while the inherited prefix contributes only `O_P(L^{3/2})=O_P(H^{3/4})`. Hence

\[
\sum_{n\le X}|B(n)|^2\ll_P H^{3/4}.
\tag{37}
\]

By the finite relation (16) and Cauchy-Schwarz,

\[
\boxed{
\sum_{n\le X}|Y(n)|^2\ll_P H^{3/4}.
}
\tag{38}
\]

This is the tail estimate needed by the Fourier skeleton.

## 4. The Fourier energy still differs from the equality ray only by lower order

At a retained horizon write

\[
x_k:=Y(\tau_H(k)),
\qquad
x_k^{(0)}:=t\frac{\mu(k)}k,
\qquad
\delta_k:=x_k-x_k^{(0)}.
\tag{39}
\]

For `1<=k<=R`, (21) and (25) give

\[
\delta_1=0,\qquad |\delta_k|\le1.
\tag{40}
\]

For `k>R`, one has `tau_H(k)<=X`. Since the floor-quotient involution is injective on `\mathcal Q_H`, (38) gives

\[
\sum_{\substack{k\in\mathcal Q_H\\k>R}}
|Y(\tau_H(k))|^2
\ll_P H^{3/4}.
\tag{41}
\]

The equality-ray tail satisfies

\[
\sum_{k>R}\left|t\frac{\mu(k)}k\right|^2
\ll
\frac{H}{R}
\ll
H^{3/4}.
\tag{42}
\]

Therefore

\[
\boxed{
\sum_{k\in\mathcal Q_H}|\delta_k|^2
\ll_P H^{3/4}.
}
\tag{43}
\]

Apply the divisor-transform stability estimate from `FD-120` to

\[
D(k):=\sum_{d\mid k}d\,\delta_d.
\tag{44}
\]

It gives

\[
\sum_{k\in\mathcal Q_H}\frac{|D(k)|^2}{k^2}
\ll_P
H^{3/4}(\log H)^2.
\tag{45}
\]

The equality ray has Fourier image supported only at `k=1`, and `D(1)=delta_1=0`; hence the cross term vanishes exactly. Equations (10)--(11) follow.

## 5. Boundary, stress tests, and prior-art audit

This theorem does **not** impose the complete Möbius sign law. The prime set `P` is fixed before the construction; its size and product may not grow with `H`. The source also need not satisfy the full divisor-identity family

\[
\sum_{d\le H}Y\!\left(\left\lfloor\frac Hd\right\rfloor\right)=1
\tag{46}
\]

at the retained horizons. Thus the result rules out finite prime breadth, not global multiplicativity or growing-depth arithmetic compatibility.

The load-bearing algebra was independently checked in finite models: the recurrence (24) reproduces every target `Y(q_d)=y_d` exactly, and the parity induction (27) agrees with direct core-squarefree counts. The asymptotic kill checks are (20), which keeps the interpolation above the frozen old prefix; (31), which leaves square-root-window capacity even at `d=QR`; and (37)--(43), which ensure that enforcing the prime directions does not move lower-order source mass back into the Fourier tail.

`FD-027` is the direct internal precursor: it introduced the finite-prime factorization and triangular inversion for the older GCD-duality geometry. No novelty is claimed for that mechanism. The new line-local content is that the same finite-prime ancestry can be made compatible simultaneously with the stronger `FD-126` package: one permanent squarefree-unit source, the exact square-root envelope, the minimal `FD-118` floor-quotient Fourier skeleton, and repeated-square near-saturation. A targeted literature search found adjacent work on multiplicative functions supported on squarefree integers, but no result addressing this Farey floor-quotient saturation construction. No external theorem is load-bearing here, so `SOURCES.md` does not change.

The research boundary is therefore sharper than after `FD-126`: **a finite menu of genuine Möbius multiplicative directions is still a matched-control relaxation**. The next candidate must have arithmetic breadth that grows with scale, or impose a genuinely global compatibility that the finite triangular inverse cannot absorb.
