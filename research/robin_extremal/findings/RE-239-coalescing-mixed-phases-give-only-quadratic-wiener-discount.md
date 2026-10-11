# RE-239 — Coalescing mixed phases give only quadratic Wiener discount

**Status:** `EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + MULTI-CENTER-SERIAL-COMPOSITION + MIXED-PHASE-STABILITY + WIENER-NORM-REPRESENTATION-OBSTRUCTION + PRIOR-ART-AUDIT`.

**Parent findings:** RE-220, RE-237.

RE-237 shows that a serial cascade of single-center predictors has exactly multiplicative Wiener cost when all centers lie on one common complex ray. The remaining serial escape is to let the center phases differ so that convolution paths reaching one output coefficient acquire different phases and can cancel.

That escape is real but perturbatively weak. If all center phases remain close to one common phase and the radii stay in a bounded set, then the logarithmic Wiener discount is at most **quadratic in the phase dispersion**.

For factors

[
a_r=ho_r e^{iarphi_r},
qquad
0<ho_rle R,
	ag{1}
]

let (F_r) be the normalized single-center polynomial of RE-237,

[
F_r(z)
=
rac{
z^{m_r}a_r^{-m_r}
displaystylesum_{k=0}^{N_r}
inom{m_r+k-1}{k}
left(1-rac{z}{a_r}ight)^k
}{
Q_r(1)
},
qquad
Q_r(1)
e0,
	ag{2}
]

and put

[
G(z):=prod_{r=1}^{J}F_r(z).
	ag{3}
]

Fix a reference phase (arphi_*), and let

[
delta_r
:=
operatorname{Arg}!left(e^{i(arphi_r-arphi_*)}ight)
in[-pi,pi].
	ag{4}
]

Then for every finite (R>0) there exist constants

[
delta_0(R)>0,
qquad
C_R<infty,
	ag{5}
]

such that whenever

[
|delta_r|ledelta_0(R)
qquad
(1le rle J),
	ag{6}
]

one has

[
oxed{
0
le
sum_{r=1}^{J}log|F_r|_A
-
log|G|_A
le
C_R
sum_{r=1}^{J}(N_r+1)delta_r^2 .
}
	ag{7}
]

Thus the exact multiplicativity of RE-237 is stable to second order under small phase splitting.

In particular, suppose

[
N_rle Lambda m_r,
qquad
M:=sum_r m_r,
	ag{8}
]

and all factors are considered on a common arc of half-width (alpha). If

[
rac{
sum_r (N_r+1)delta_r^2
}{
Malpha
}
longrightarrow0,
	ag{9}
]

then

[
oxed{
rac{log|G|_A}{Malpha}
=
sum_r
rac{m_r}{M}
rac{log|F_r|_A}{m_ralpha}
+
o(1).
}
	ag{10}
]

Consequently a mixed-phase serial architecture cannot improve the leading Wiener exponent merely by perturbing a co-phased cascade. For a fixed positive arc width, any phase family with

[
max_r|delta_r|	o0
	ag{11}
]

and bounded truncation ratios satisfies (9). If the arc itself shrinks, the sufficient scale is

[
max_rdelta_r^2=o(alpha).
	ag{12}
]

At the microscopic scale

[
max_r|delta_r|=O(M^{-1/2}),
	ag{13}
]

the total logarithmic discount is only (O(1)) under bounded truncation ratios, hence is negligible whenever (Malpha	oinfty).

This does **not** rule out genuinely separated mixed phases, parallel/minimax synthesis, or a coupled product whose useful interference is nonperturbative. It identifies a local rigidity boundary around the exact same-ray obstruction of RE-237.

## 1. The RE-237 coefficient law converts phase splitting into characteristic functions

For one factor, RE-237 gives

[
[z^{m+j}]F
=
gamma,omega^j B_j,
qquad
omega=-e^{-iarphi},
qquad
B_j>0,
	ag{14}
]

where

[
B_j
=
ho^{-j}
sum_{k=j}^{N}
inom{m+k-1}{k}
inom{k}{j}.
	ag{15}
]

Put

[
S:=sum_{j=0}^{N}B_j,
qquad
p_j:=rac{B_j}{S}.
	ag{16}
]

Then

[
|F|_A
=
|gamma|S.
	ag{17}
]

Let

[
omega_*:=-e^{-iarphi_*},
qquad
z_*:=omega_*^{-1}.
	ag{18}
]

Since (|z_*|=1), evaluation on the unit circle is dominated by Wiener norm. For the factor with phase displacement (delta=arphi-arphi_*),

[
omega z_*
=
e^{-idelta}.
	ag{19}
]

Hence, up to a unit-modulus monomial factor,

[
|F(z_*)|
=
|F|_A
left|
sum_{j=0}^{N}p_j e^{-ijdelta}
ight|.
	ag{20}
]

Define the characteristic function

[
chi(delta)
:=
sum_{j=0}^{N}p_j e^{-ijdelta}.
	ag{21}
]

Applying (20) to every stage and using (|G|_Age |G(z_*)|),

[
|G|_A
ge
prod_r
|F_r|_A
|chi_r(delta_r)|.
	ag{22}
]

The usual Wiener-algebra inequality gives the reverse multiplicative upper bound,

[
|G|_A
le
prod_r|F_r|_A.
	ag{23}
]

Therefore the entire mixed-phase discount satisfies the exact sandwich

[
oxed{
0
le
D
:=
sum_rlog|F_r|_A-log|G|_A
le
sum_r -log|chi_r(delta_r)|.
}
	ag{24}
]

The remaining problem is thus one-dimensional: control the characteristic function of the positive coefficient-modulus distribution of each single-center factor.

## 2. The coefficient-modulus law is a binomial mixture with a geometrically thin depth defect

From (15),

[
sum_{j=0}^{N}B_j z^j
=
sum_{k=0}^{N}
inom{m+k-1}{k}
left(1+rac{z}{ho}ight)^k.
	ag{25}
]

Set

[
A:=1+rac1ho,
qquad
p:=rac1{ho+1}.
	ag{26}
]

Define a random variable (Kin{0,ldots,N}) by

[
mathbf P(K=k)
=
rac{
inom{m+k-1}{k}A^k
}{
displaystyle
sum_{ell=0}^{N}
inom{m+ell-1}{ell}A^ell
}.
	ag{27}
]

Conditional on (K=k), let

[
Jmid K=k
sim
operatorname{Binomial}(k,p).
	ag{28}
]

Then the probability generating function of (J) is exactly

[
mathbf E z^J
=
rac{
displaystyle
sum_{k=0}^{N}
inom{m+k-1}{k}
left(1+rac{z}{ho}ight)^k
}{
displaystyle
sum_{k=0}^{N}
inom{m+k-1}{k}
left(1+rac1hoight)^k
},
	ag{29}
]

so

[
oxed{
mathbf P(J=j)=p_j
}
	ag{30}
]

and (chi(delta)=mathbf E e^{-idelta J}).

The useful feature is that (K) is concentrated near the truncation edge (N). Write

[
D_0:=N-K.
	ag{31}
]

If

[
w_k:=inom{m+k-1}{k}A^k,
	ag{32}
]

then

[
rac{w_{k-1}}{w_k}
=
rac{k}{m+k-1}rac1A
le
rac{ho}{ho+1}.
	ag{33}
]

For (0<hole R), put

[
q_R:=rac{R}{R+1}<1.
	ag{34}
]

Since the normalizing sum in (27) is at least (w_N), (33) yields the uniform defect bound

[
oxed{
mathbf P(D_0=d)
le
q_R^d
qquad(dge0).
}
	ag{35}
]

Thus every exponential moment of (D_0) in a fixed neighborhood of zero is bounded by a constant depending only on (R), uniformly in (m,N).

Equation (35) is the only distributional input needed below. No asymptotic formula for a truncated negative-binomial variance is required.

## 3. Uniform quadratic control of the characteristic function

Put

[
z(delta)
:=
1-p+p e^{-idelta}.
	ag{36}
]

Conditioning on (K),

[
chi(delta)
=
mathbf E z(delta)^K
=
z(delta)^N
mathbf E z(delta)^{-D_0}.
	ag{37}
]

The first factor has an explicit modulus:

[
|z(delta)|^2
=
1-4p(1-p)sin^2rac{delta}{2}.
	ag{38}
]

Hence for (|delta|le1),

[
-log|z(delta)|
le
C,delta^2
	ag{39}
]

with an absolute constant (C).

It remains to control

[
H(delta)
:=
mathbf E z(delta)^{-D_0}.
	ag{40}
]

By (35), choose a fixed complex neighborhood of (u=1) in which

[
q_R|u|<1.
	ag{41}
]

Uniformly over all admissible (m,N,ho), the generating functions

[
h(u):=mathbf E u^{D_0}
	ag{42}
]

and their first two derivatives are bounded there by geometric-series majorants. Since

[
h(1)=1,
	ag{43}
]

there is a smaller neighborhood on which (h) has no zero and a single analytic logarithm can be chosen uniformly.

Now

[
u(delta):=z(delta)^{-1}
	ag{44}
]

satisfies (u(0)=1), while (u'(0)) is purely imaginary. Because (h'(1)=mathbf E D_0) is real,

[
rac{d}{ddelta}
operatorname{Re}
log h(u(delta))
igg|_{delta=0}
=0.
	ag{45}
]

The uniform bounds on (h,h',h''), together with the smoothness of (u), therefore give constants (delta_0(R)>0) and (C'_R) such that

[
left|
log|H(delta)|
ight|
le
C'_Rdelta^2
qquad
(|delta|ledelta_0(R)).
	ag{46}
]

Combining (37), (39), and (46),

[
oxed{
-log|chi(delta)|
le
C_R(N+1)delta^2
}
	ag{47}
]

for a possibly larger (C_R).

Substituting (47) into (24) proves (7).

The proof is finite and uniform. It does not use a central-limit approximation, a Gaussian ansatz, a fixed number of stages, or an asymptotic formula for the truncated distribution.

## 4. Consequence for the separated-prediction exponent

Assume the truncation ratios are uniformly bounded,

[
N_rleLambda m_r.
	ag{48}
]

Since (m_rge1), the number of factors satisfies (Jle M). Equation (7) gives

[
D
le
C_R
sum_r(N_r+1)delta_r^2.
	ag{49}
]

Dividing by (Malpha),

[
oxed{
0
le
sum_r
rac{m_r}{M}
rac{log|F_r|_A}{m_ralpha}
-
rac{log|G|_A}{Malpha}
le
rac{C_R}{Malpha}
sum_r(N_r+1)delta_r^2.
}
	ag{50}
]

This proves (10) under (9).

A simple sufficient condition is

[
max_rdelta_r^2=o(alpha),
	ag{51}
]

because

[
sum_r(N_r+1)
le
(Lambda+1)M.
	ag{52}
]

For the fixed-arc families used in the explicit separated-prediction constructions, (alphaasymp1), so **any coalescing family of center phases** has the same leading Wiener exponent as its co-phased reference cascade.

At the sharper scale

[
max_rdelta_r^2=O(M^{-1}),
	ag{53}
]

the total discount in (49) is (O(1)). Hence if (Malpha	oinfty), a phase splitting of order (M^{-1/2}) cannot alter the normalized exponent even by a fixed positive amount.

This is the perturbative boundary needed for the next architectural decision. To lower the approximately (5.996390) constructive constant by a nonvanishing amount through serial coefficient cancellation, the phase geometry must be **macroscopically non-coalescing relative to the observation scale**.

## 5. Stress tests and failure boundaries

### Genuinely separated phases remain open

RE-237 already supplies a finite example where different phases give strict Wiener submultiplicativity. Equation (7) is local around one common ray. It does not rule out order-one phase separation, and it does not claim that the best mixed-phase serial cascade has the same cost as the co-phased family.

### Unbounded radii are not covered uniformly

The bounded-radius hypothesis is load-bearing for the uniform geometric defect estimate (35). As (ho	oinfty),

[
rac{ho}{ho+1}	o1,
]

so the depth defect (D_0=N-K) need not retain a uniform exponential tail. The large-center regimes were analyzed separately in RE-230--RE-236 and are not silently folded into this perturbative theorem.

### The norm theorem does not require factorwise prediction

Equation (7) is purely a coefficient/norm statement. It holds even when the individual factors do not approximate one. Thus a coupled product cannot obtain a large Wiener discount from *small* phase splitting merely by abandoning factorwise prediction.

However, the interpretation of the right side of (10) as an average of constituent **predictor rates** requires the factors themselves to satisfy the relevant prediction conditions. A genuinely coupled product may still obtain its approximation property in a way not visible stage by stage.

### Shrinking arcs require the correct scale comparison

For (alpha	o0), merely assuming (delta_r	o0) is insufficient. The relevant quantity is the right side of (50). Condition (51), or the more precise weighted condition (9), is what makes the Wiener discount negligible relative to the normalization (Malpha).

### The quadratic order is natural

The first derivative of the logarithmic modulus vanishes at the co-phased point because the coefficient-modulus distribution has a real first moment while the phase perturbation enters tangentially to the unit circle. The first possible loss of modulus is therefore second order. This is exactly the mechanism made quantitative in (45)--(47).

## 6. Prior-art and representation audit

Three generic ingredients are classical:

1. the Wiener algebra is a Banach algebra and its norm is submultiplicative under multiplication;
2. characteristic functions have second-order behavior controlled by second moments near the origin;
3. moments of truncated negative-binomial laws have a substantial probability/statistics literature.

A targeted search located, among other standard references, J. S. Shonkwiler, *Variance of the truncated negative binomial distribution*, Journal of Econometrics **195** (2016), 209--210, DOI `10.1016/j.jeconom.2016.09.002`. That paper is useful prior-art context for truncated count-law moments, but it is not load-bearing here. Equation (35) supplies the only moment control needed, directly from the exact Mathia coefficient weights.

Likewise, no novelty is claimed for the elementary characteristic-function fact that a centered finite-variance law has no first-order loss of modulus. The line-specific content is the exact sequence

[
	ext{single-center coefficient law}
longrightarrow
	ext{binomial-mixture modulus distribution}
longrightarrow
	ext{common-circle evaluation}
longrightarrow
	ext{quadratic mixed-phase Wiener discount}.
	ag{54}
]

A broad search did not locate this particular consequence for serial off-center negative-binomial predictors. No external theorem is needed to prove (7), so `SOURCES.md` requires no update.

## Research consequence

RE-237 rules out same-ray serial multi-center synthesis exactly. RE-239 now rules out its entire **perturbative mixed-phase neighborhood** at leading Wiener exponent.

Thus a serial multi-center construction intended to improve the current explicit upper bound

[
C_{m sep}le5.996390
]

must generate a phase spread large enough that

[
rac{
sum_r(N_r+1)delta_r^2
}{
Malpha
}

ot	o0,
	ag{55}
]

or exploit a different architecture altogether.

The next decision-relevant search should therefore not optimize tiny phase offsets around the positive-real/same-ray construction. It should test genuinely separated mixed phases, parallel/additive minimax synthesis, or another representation in which coefficient paths meet with order-one phase disagreement before absolute values are taken.
