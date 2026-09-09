# FD-008 — joint squarefree signs and one exact divisor identity still do not improve the leading Franel--Mertens dual constant

**Status:** `EXACT-DERIVED + JOINT-SQUAREFREE-SIGN-DIVISOR-COMPATIBILITY + DISCRETE-REPAIR + SHARP-ASYMPTOTIC-DUALITY + NEGATIVE/OBSTRUCTION`. `FD-007` proves that the exact squarefree support and unit-amplitude restrictions on a synthetic Möbius-like increment sequence do not improve the leading coordinate constant of the Franel--Mertens GCD energy, but its signs need not satisfy the physical divisor identity isolated in `FD-005`. Imposing these restrictions **simultaneously** still does not create a persistent gap.

For

\[
K_N(d,e)=\frac{\gcd(d,e)^2}{de},
\qquad
A_a(x)=\sum_{n\le x}a_n,
\qquad
m_d(a)=A_a\!\left(\left\lfloor\frac Nd\right\rfloor\right),
\]

let `mathcal U_N^div` be the class of increment sequences satisfying

\[
a_1=1,
\qquad
a_n=0\quad(n\text{ nonsquarefree}),
\qquad
a_n\in\{-1,+1\}\quad(n\text{ squarefree}),
\tag{1}
\]

and the exact fixed-horizon divisor compatibility

\[
\sum_{d=1}^Nm_d(a)=1,
\qquad\text{equivalently}\qquad
\sum_{n\le N}a_n\left\lfloor\frac Nn\right\rfloor=1.
\tag{2}
\]

Define

\[
\Theta_N^{\rm div}
:=\max_{a\in\mathcal U_N^{\rm div}}
\frac{m_1(a)^2}{m(a)^TK_Nm(a)}.
\tag{3}
\]

Then

\[
\boxed{
\Theta_N^{\rm div}\longrightarrow\zeta(2)=\frac{\pi^2}{6}.
}
\tag{4}
\]

More quantitatively,

\[
\boxed{
0\le\zeta(2)-\Theta_N^{\rm div}\ll N^{-1/10}.
}
\tag{5}
\]

Thus the intersection left open by `FD-006` and `FD-007` is still asymptotically sharp. The exact squarefree zero pattern, unit signs on every squarefree integer, `a_1=1`, and the single exact divisor identity (2) together do not improve the RH-facing leading homogeneous scalar coefficient after cumulative Farey information has been compressed to the `FD-003` GCD energy. A further cumulative argument must use genuinely deeper correlation of the Möbius signs, growing-depth compatibility, multiplicativity/divisor structure beyond one horizon identity, or another nonlinear source restriction. Ordered Farey information before cumulative shell collapse remains separate.

## 1. Start from the zero-sum principal extremizer, not the unrestricted one

Let

\[
R=\lfloor N^{1/5}\rfloor,
\qquad
q_d=\left\lfloor\frac Nd\right\rfloor,
\qquad
Q=q_{R+1}.
\tag{6}
\]

Write `K_R` for the `R x R` principal square-GCD matrix and retain the exact quantities of `FD-005`,

\[
C_R=e_1^TK_R^{-1}e_1,
\qquad
A_R=e_1^TK_R^{-1}\mathbf1,
\qquad
B_R=\mathbf1^TK_R^{-1}\mathbf1.
\tag{7}
\]

The `K_R`-Riesz representer of the first coordinate inside the zero-total-sum hyperplane is

\[
v^{(R)}
:=K_R^{-1}e_1-rac{A_R}{B_R}K_R^{-1}\mathbf1.
\tag{8}
\]

Consequently

\[
\boxed{
\mathbf1^Tv^{(R)}=0,
\qquad
v_1^{(R)}=(v^{(R)})^TK_Rv^{(R)}=C_R^{(0)},
}
\tag{9}
\]

where

\[
C_R^{(0)}=C_R-\frac{A_R^2}{B_R}
\]

and `FD-005` proves

\[
\boxed{
0\le\zeta(2)-C_R^{(0)}\ll\frac{(\log R)^2}{R}.
}
\tag{10}
\]

This zero-sum choice is the structural change needed for the joint problem. If the first `R` hyperbola-block values are made close to a large multiple of `v^(R)`, their contribution to the divisor identity has no large main term.

The vector still has bounded local oscillation. `FD-007` gives, for `u=K_R^{-1}e_1`,

\[
|u_d|\le\frac{\zeta(2)^2}{d}.
\tag{11}
\]

For `w=K_R^{-1}\mathbf1`, Smith--Jordan inversion gives

\[
w_d
=d\sum_{\substack{r\le R\\d\mid r}}
\frac{\mu(r/d)\varphi(r)}{J_2(r)}.
\tag{12}
\]

Since

\[
\frac{\varphi(r)}{J_2(r)}
=\frac1r\prod_{p\mid r}\frac1{1+1/p}
\le\frac1r,
\]

one has

\[
|w_d|\le H_{\lfloor R/d\rfloor}\le1+\log(R/d).
\tag{13}
\]

Together with `FD-005`'s `A_R/B_R=O((\log R)/R)`, equations (11)--(13) show that, for all sufficiently large `R`, both `|v_d^(R)|` and the successive differences `|v_d^(R)-v_(d+1)^(R)|` are bounded by an absolute constant. No cancellation estimate for the true Möbius function is used here.

## 2. A bounded tail can also have only `O(R)` divisor workload

The lower part `n<=Q` must satisfy two requirements simultaneously: every squarefree integer must receive a sign, while both its ordinary partial sums and its contribution to (2) remain small. A four-dilate cancellation provides this without probabilistic input.

Let

\[
\mathcal C_Q
:=\{r\le Q:r\text{ squarefree and }(r,6)=1\}.
\tag{14}
\]

Order these `r` increasingly. Assign signs `epsilon_r in {+-1}` in consecutive pairs, with opposite signs inside every pair. Fix the first pair orientation so `epsilon_1=+1`; for the remaining pairs the orientation will be chosen below. If one core point remains unpaired at the end, its sign is free. Put

\[
E(x):=\sum_{\substack{r\le x\\r\in\mathcal C_Q}}\varepsilon_r.
\tag{15}
\]

Pairing gives

\[
|E(x)|\le1
\qquad(x\ge0).
\tag{16}
\]

Every squarefree `n` has a unique representation `n=dr` with

\[
d\in\{1,2,3,6\},\qquad r\in\mathcal C_Q.
\]

Set

\[
\chi(1)=1,
\qquad
\chi(2)=\chi(3)=\chi(6)=-1,
\qquad
a_{dr}=\chi(d)\varepsilon_r
\quad(dr\le Q),
\tag{17}
\]

and put `a_n=0` on nonsquarefree integers. This assigns amplitude one to **every** squarefree integer below `Q` and keeps `a_1=1`. Its partial sums satisfy the exact identity

\[
A_a(x)
=E(x)-E(x/2)-E(x/3)-E(x/6),
\tag{18}
\]

hence

\[
\boxed{|A_a(x)|\le4\qquad(1\le x\le Q).}
\tag{19}
\]

The same four-dilate pattern controls the divisor workload. Define

\[
c(r)
:=\left\lfloor\frac Nr\right\rfloor
-\mathbf1_{2r\le Q}\left\lfloor\frac N{2r}\right\rfloor
-\mathbf1_{3r\le Q}\left\lfloor\frac N{3r}\right\rfloor
-\mathbf1_{6r\le Q}\left\lfloor\frac N{6r}\right\rfloor.
\tag{20}
\]

Then the tail contribution is

\[
W_{\rm tail}
:=\sum_{n\le Q}a_n\left\lfloor\frac Nn\right\rfloor
=\sum_{r\in\mathcal C_Q}\varepsilon_r c(r).
\tag{21}
\]

For `r<=Q/6`, all four dilates are present and the real main terms cancel because

\[
1-\frac12-\frac13-\frac16=0.
\tag{22}
\]

Only floor errors remain, so `|c(r)|<=4`. For `r>Q/6`, the trivial estimate and `N/Q=O(R)` give

\[
|c(r)|=O(R).
\tag{23}
\]

Thus `M_Q:=max_r|c(r)|=O(R)`. For every core pair `{r,r'}`, its contribution to (21) is `+-[c(r)-c(r')]`. After the fixed first pair, choose each pair orientation greedily to minimize the current absolute weighted sum. Since `|c(r)-c(r')|<=2M_Q`, induction keeps the running total at most `2M_Q`; an unpaired final point can be signed to preserve the same order. Therefore

\[
\boxed{W_{\rm tail}=O(R).}
\tag{24}
\]

The tail construction is entirely synthetic and deliberately nonmultiplicative. Its role is to prove sharpness of the declared relaxation, not to model the actual Möbius signs.

## 3. Encode the growing principal extremizer in the hyperbola intervals

For `1<=d<=R`, let

\[
I_d=(q_{d+1},q_d]\cap\mathbb Z,
\qquad
L_d=|I_d|,
\qquad
L_*=\min_{d\le R}L_d.
\tag{25}
\]

As in `FD-007`,

\[
L_*\asymp\frac N{R^2}\asymp N^{3/5},
\tag{26}
\]

and an elementary union bound for square divisibility gives a constant `c_0>0` such that every `I_d` contains at least `c_0L_d` squarefree integers for all sufficiently large `N`.

Choose a sufficiently small fixed `kappa>0` and set

\[
t_N=\kappa L_*\asymp N^{3/5}.
\tag{27}
\]

For each `d<=R`, choose an integer `y_d` of the parity forced by the number of squarefree integers up to `q_d`, with

\[
|y_d-t_Nv_d^{(R)}|\le1.
\tag{28}
\]

Set

\[
y_{R+1}:=A_a(Q),
\tag{29}
\]

where the right side is supplied by the tail of Section 2, so `|y_(R+1)|<=4` and its parity is automatically correct. Put `Delta_d=y_d-y_(d+1)`. Because `v^(R)` has uniformly bounded successive differences, `kappa` can be chosen so that

\[
|\Delta_d|\le S_d,
\tag{30}
\]

where `S_d` is the number of squarefree integers in `I_d`. The parity of `Delta_d` is exactly the parity of `S_d`. Hence the squarefree integers in every `I_d` can be assigned `+-1` signs with total `Delta_d`; all nonsquarefree integers receive zero. Telescoping then gives

\[
\boxed{m_d(a)=A_a(q_d)=y_d\qquad(1\le d\le R).}
\tag{31}
\]

For `d>R`, `q_d<=Q`, so (19) gives

\[
|m_d(a)|\le4.
\tag{32}
\]

At this point every position `1<=n<=N` satisfies the exact squarefree support/amplitude conditions (1), but the divisor identity has not yet been repaired.

## 4. The remaining divisor defect is only `O(R)` and can be repaired exactly

Let

\[
W:=\sum_{n\le N}a_n\left\lfloor\frac Nn\right\rfloor.
\tag{33}
\]

On `I_d`, one has `floor(N/n)=d`. Therefore

\[
W
=W_{\rm tail}+\sum_{d=1}^R d\Delta_d.
\tag{34}
\]

Discrete summation by parts gives

\[
\sum_{d=1}^Rd(y_d-y_{d+1})
=\sum_{d=1}^Ry_d-Ry_{R+1}.
\tag{35}
\]

Now `sum_(d<=R)v_d^(R)=0` by (9), each rounding error in (28) is at most one, `y_(R+1)=O(1)`, and `W_tail=O(R)`. Consequently

\[
\boxed{W=O(R).}
\tag{36}
\]

Put `D=1-W`. The defect is even. Indeed any legal sequence satisfying (1) is congruent modulo two to the squarefree indicator, while the actual Möbius sequence has the same support parity and satisfies the exact identity (2). Hence `W congruent 1 (mod 2)` and

\[
D\in2\mathbb Z,
\qquad
|D|=O(R).
\tag{37}
\]

Repair the defect only inside

\[
I_1=(\lfloor N/2\rfloor,N].
\]

Every point there has divisor weight one. Flipping one squarefree sign changes `W` by exactly `+-2` and changes only `m_1`, leaving every `m_d`, `d>=2`, untouched. The interval contains `gg N` squarefree integers, while its prescribed total `Delta_1=O(t_N)` and `|D|=O(R)=o(N)`. Thus both sign choices occur in quantities far exceeding `|D|/2`. Flip exactly `|D|/2` signs of the appropriate orientation. The repaired sequence satisfies

\[
\boxed{W=1,}
\tag{38}
\]

so it belongs to `mathcal U_N^div`. The repair changes the staircase by exactly

\[
\delta m=D e_1,
\qquad
|D|=O(R)=o(t_N).
\tag{39}
\]

This exact one-weight repair is why the single fixed-horizon divisor identity does not obstruct the discrete sign realization.

## 5. The exact repair is negligible in the GCD energy

Pad `v^(R)` by zeros through coordinate `N` and call the result `w^(N)`. Before the final repair, equations (28), (31), and (32) give

\[
m(a)=t_Nw^{(N)}+z^{(N)},
\qquad
|z_d^{(N)}|\le4.
\tag{40}
\]

`FD-007` proves the Smith--Jordan bound

\[
\mathbf1^TK_N\mathbf1\ll N.
\tag{41}
\]

Since `K_N` has nonnegative entries, (40) implies

\[
\|z^{(N)}\|_{K_N}=O(\sqrt N).
\tag{42}
\]

The exact repair (39) has `K_N`-norm `O(R)`, which is smaller. Thus the final exactly feasible staircase has

\[
\boxed{
m=t_Nw^{(N)}+e^{(N)},
\qquad
\|e^{(N)}\|_{K_N}=O(\sqrt N),
\qquad
e_1^{(N)}=O(R).
}
\tag{43}
\]

Because the principal vector has

\[
(w^{(N)})^TK_Nw^{(N)}=w_1^{(N)}=C_R^{(0)},
\tag{44}
\]

and `t_N asymp N^(3/5)`, Cauchy--Schwarz in the `K_N` norm yields

\[
\frac{m_1^2}{m^TK_Nm}
\ge
C_R^{(0)}-O\!\left(\frac{\sqrt N}{t_N}\right)
=C_R^{(0)}-O(N^{-1/10}).
\tag{45}
\]

On the other hand `mathcal U_N^div subset mathcal U_N`, and `FD-007` bounds the latter class by the unrestricted coordinate constant, so

\[
\Theta_N^{\rm div}\le\zeta(2).
\tag{46}
\]

Combining (10), (45), and `R=N^(1/5)+O(1)` proves (5), hence (4).

## 6. Prior art, falsification controls, and evidence boundary

The divisor identity itself is classical Möbius inversion and is already anchored in `FD-005` through Deléglise--Rivat. The Smith/Jordan projection used in Section 1 is also already canonical in `FD-003`--`FD-005`. The new argument does not import a stronger analytic theorem: its additional ingredients are parity, elementary squarefree density in the long hyperbola intervals, the four-dilate identity (22), and a finite greedy signing of paired core points.

A targeted literature audit also checked the neighboring theory of squarefree-supported sign sequences. Marco Aymone, *The Erdős discrepancy problem over the squarefree and cubefree integers*, Mathematika **68** (2022), 51--73, DOI `10.1112/mtk.12117`, proves unboundedness phenomena for squarefree-supported signs under **complete multiplicativity**. That does not conflict with the bounded synthetic tail above: the `epsilon_r` are freely paired and are explicitly not required to obey a multiplicative law. This distinction is load-bearing and is precisely why multiplicative/sign-correlation compatibility remains available after the present relaxation is closed. No theorem from that paper is used in the proof.

Several controls prevent overinterpretation. First, the constructed sequence depends on `N`; it disproves a uniform improvement on the declared fixed-horizon relaxation but does not claim that one infinite sign sequence simultaneously saturates every horizon. Second, satisfying one divisor identity does not imply the full Jordan hierarchy, multiplicativity, or the actual law `mu(n)=(-1)^{omega(n)}`. Third, the exact repair exploits the weight-one interval `I_1`; imposing a growing family of prefix identities could remove this freedom and is not covered here. Fourth, the result is homogeneous: a different nonhomogeneous inequality exploiting the affine offset may still contain information even though the leading scalar coefficient is unchanged.

Finally, (4)--(5) concern only the auxiliary sharp constant after cumulative compression. They do not improve the Franel discrepancy bound, prove a new Mertens estimate, or advance the RH exponent directly. Their durable consequence is negative but useful: **support/amplitude and one exact divisor identity do not become stronger merely by being imposed jointly**. The next cumulative theorem must use a source constraint whose interaction cannot be repaired at negligible GCD-energy cost, or the research must retain ordered Farey structure before this compression.
