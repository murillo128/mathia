# XF-081 — Chebyshev nullspace makes the center-local Vieta state nonidentifiable

**Status:** `EXACT-DERIVED` + `SOURCE-DICTIONARY-NO-GO` + `CENTER-LOCAL-CHEBYSHEV-NULLSPACE` + `Vieta-PREFIX-PRESCRIPTION`. XF-078 shows that the matched Gaussian-reference quotient can be approximated on the center Xi high line by an ordinary `N+1`-mode trigonometric polynomial, while XF-080 shows that the particular explicit binomial surrogate used there is unusable as a Vieta carrier: after outer normalization its first root-power mode is `Theta(N)` and its terminal coefficient is not unimodular. A natural repair would be to choose a different center-local surrogate whose outer coefficient and low Vieta modes are well conditioned.

At the static center-local level that repair is not merely possible; it is **far too nonunique to define the Vieta state**. There is an explicit Chebyshev family which is exponentially small on the center half-period but carries order-one prescribed outer Fourier coefficients. Using a triangular pair of such null functions, one can alter the XF-078 approximant by `exp(-cN)` on the actual shrinking Xi high-line rectangle while prescribing an arbitrarily long growing prefix of its normalized Vieta coefficients.

More precisely, write the XF-078 integer-frequency surrogate as

\[
A_D(\theta)=\sum_{m=-D}^{D}p_{m,D}e^{im\theta},
\qquad N=2D,
\tag{1}
\]

with `D=M=q^2`. Let `K=K(D)` satisfy

\[
K\log D=o(D).
\tag{2}
\]

Then there is another Laurent polynomial

\[
B_D(\theta)=\sum_{m=-D}^{D}b_{m,D}e^{im\theta}
\tag{3}
\]

such that

\[
\boxed{
b_{D,D}=b_{-D,D}=1,
\qquad
b_{D-r,D}=b_{-D+r,D}=0
\quad(1\le r\le K),
}
\tag{4}
\]

and, for every fixed derivative order `J`, on the actual Xi center high line

\[
|\Re\theta|\le\frac\pi2,
\qquad
|\Im\theta|\le C D^{-1/2},
\tag{5}
\]

one has

\[
\boxed{
\max_{0\le j\le J}
\sup_{(5)}
|\partial_\theta^j(B_D-A_D)|
\le
\exp(-c_JD)
}
\tag{6}
\]

for all sufficiently large `D`. Hence `B_D` has the same `exp(-cD)` center-local accuracy for the matched quotient as XF-078.

But in the centered Vieta normalization of XF-067,

\[
G(\theta)
=A_0\sum_{r=0}^{N}(-1)^rE_r e^{i(D-r)\theta},
\tag{7}
\]

conditions (4) give

\[
\boxed{
E_0=E_N=1,
\qquad
E_r=E_{N-r}=0
\quad(1\le r\le K).
}
\tag{8}
\]

Newton identities then force

\[
\boxed{P_1=P_2=\cdots=P_K=0.}
\tag{9}
\]

At the Xi scale the full source-visible/guarded Vieta range has

\[
K_T=O(q\log\log T),
\qquad
D=q^2,
\tag{10}
\]

so `K_T log D=o(D)`. Thus one may make **every Vieta power sum through the entire XF-070--XF-071 source band vanish exactly** while changing the center-local matched function by only `exp(-c q^2)`.

This is the opposite extreme from XF-080, whose equally accurate explicit surrogate has `P_1=Theta(D)` and an order-one contribution to the normalized low-mode resource. Therefore center-local `C^J` accuracy of the carrier function does not determine, or even stably constrain, the Vieta resource needed by XF-070--XF-071. Adding outer normalization or finitely/growingly many low-Vieta conditioning constraints to a static approximation theorem cannot by itself create a source-faithful dictionary: those constraints can be imposed almost for free by functions invisible on the center window.

The live bridge must consequently use information not contained in static center-local function approximation alone: for example a root-faithful construction, a heat-compatible global/divisor constraint, or a direct map from the Gaussian quotient/logarithmic derivative to the one-center selector of XF-079. The finding is a dictionary obstruction, not an obstruction to the Gaussian-reference route itself and not an upper bound on `Lambda`.

## 1. An exponentially invisible basis with prescribed outer modes

Put

\[
y(\theta):=2\cos\theta-1
=e^{i\theta}+e^{-i\theta}-1.
\tag{11}
\]

For `n>=1`, define two elementary trigonometric polynomials from the Chebyshev polynomials of the first and second kinds:

\[
\boxed{
C_n(\theta)
:=2^{1-n}T_n(y(\theta)),
}
\tag{12}
\]

and

\[
\boxed{
S_n(\theta)
:=2^{1-n}(e^{i\theta}-e^{-i\theta})
U_{n-1}(y(\theta)).
}
\tag{13}
\]

Since `T_n` has leading coefficient `2^{n-1}` and `U_{n-1}` has leading coefficient `2^{n-1}`, their outer Laurent coefficients are exactly

\[
[e^{in\theta}]C_n=[e^{-in\theta}]C_n=1,
\tag{14}
\]

and

\[
[e^{in\theta}]S_n=1,
\qquad
[e^{-in\theta}]S_n=-1.
\tag{15}
\]

Thus `C_n` changes the two outer coefficients in the same direction, while `S_n` changes them in opposite directions.

On the real center half-period,

\[
|\theta|\le\frac\pi2,
\tag{16}
\]

one has `cos theta in [0,1]`, hence

\[
y(\theta)\in[-1,1].
\tag{17}
\]

The elementary Chebyshev bounds

\[
|T_n(y)|\le1,
\qquad
|U_{n-1}(y)|\le n
\qquad(-1\le y\le1)
\tag{18}
\]

therefore give

\[
\boxed{
\|C_n\|_{L^\infty(16)}\le2^{1-n},
\qquad
\|S_n\|_{L^\infty(16)}\le n\,2^{2-n}.
}
\tag{19}
\]

So an order-one change in an outer Laurent coefficient costs only `Theta(2^{-n})` on the center interval. This is the basic nullspace missed by interpreting one particular XF-078 approximant as a canonical carrier.

Fixed center derivatives remain exponentially small. Differentiating (12)--(13) and using the standard polynomial bounds following directly from the trigonometric representations of `T_n` and `U_n` gives, for each fixed `J`,

\[
\max_{j\le J}
\sup_{|\theta|\le\pi/2}
\left(
|\partial_\theta^jC_n|
+|\partial_\theta^jS_n|
\right)
\le
C_J n^{2J+2}2^{-n}.
\tag{20}
\]

No approximation theorem is needed for (19)--(20); they follow from the explicit Chebyshev formulas.

## 2. The nullspace survives on the actual shrinking Xi high line

XF-078 uses a fixed complex rectangle to prove the original approximation, but the actual Xi contour lies much closer to the real axis. In its notation

\[
\left|\Im\theta\right|
=\left|\frac{2\pi\Im z}{L}\right|
=O((\log T)^{-2}).
\tag{21}
\]

Since `D=Theta((log T)^4)`, this is exactly

\[
|\Im\theta|=O(D^{-1/2}).
\tag{22}
\]

For `theta=x+i eta` with `|x|<=pi/2`, the point `y(theta)` lies at Euclidean distance `O(|eta|)` from `[-1,1]`. The elementary representation

\[
T_n(y)=\frac12\left(\zeta^n+\zeta^{-n}\right),
\qquad
\zeta=y+\sqrt{y^2-1},
\tag{23}
\]

shows uniformly in such a neighborhood that

\[
\log^+|\zeta|\le C\sqrt{|\eta|}.
\tag{24}
\]

The analogous formula for `U_{n-1}` has only an additional polynomial factor in `n` and `|eta|^{-1/2}`. Hence, for fixed `J`, `n` in a terminal block `D-K<=n<=D`, and `|eta|<=C_0D^{-1/2}`,

\[
\boxed{
\max_{j\le J}
\sup_{\substack{|x|\le\pi/2\\|\eta|\le C_0D^{-1/2}}}
\left(
|\partial_\theta^jC_n(x+i\eta)|
+|\partial_\theta^jS_n(x+i\eta)|
\right)
\le
D^{C_J}2^{-n}
\exp(C_J nD^{-1/4}).
}
\tag{25}
\]

The extra complex growth is `exp(O(D^(3/4)))=exp(o(D))`, while the real-center suppression is `2^{-n}=exp(-(log 2)n)`. Therefore every terminal Chebyshev null function remains exponentially invisible on the **actual** Xi high line as long as `D-n=o(D)`.

This shrinking-strip qualification is load-bearing. The present argument does not say that the corrections remain small on the whole fixed-height complex rectangle of XF-078; they need not. The source interface, however, is evaluated on (21), where the exponential margin is intact.

## 3. A triangular construction prescribes both Vieta edges

Write

\[
C_n(\theta)=\sum_{m=-n}^{n}c^{(+)}_{n,m}e^{im\theta},
\qquad
S_n(\theta)=\sum_{m=-n}^{n}c^{(-)}_{n,m}e^{im\theta}.
\tag{26}
\]

Besides the exact outer coefficients (14)--(15), the near-edge coefficients grow only polynomially per step away from the edge. One convenient crude form is

\[
\boxed{
|c^{(\pm)}_{n,n-r}|+|c^{(\pm)}_{n,-n+r}|
\le (C n)^{r+1},
\qquad 0\le r\le n.
}
\tag{27}
\]

For `C_n`, this follows directly from the normalized Chebyshev recurrence

\[
C_{n+1}
=(e^{i\theta}+e^{-i\theta}-1)C_n
-\frac14C_{n-1},
\tag{28}
\]

starting from the outer coefficient one. The same induction applied to the second-kind recurrence gives (27) for `S_n`. The precise polynomial constant is irrelevant; the point is that moving `r` places inward costs only `exp(O(r log n))`, not `exp(cn)`.

The explicit XF-078 approximant `A_D` itself has polynomially bounded real-circle norm: in its binomial representation, `|nu|<=1`, the coefficients of `(1-nu)^(1/2)` are absolutely summable, and

\[
b_n=4^{-n}{2n\choose n}=O(n^{-1/2}).
\tag{29}
\]

Thus

\[
\|A_D\|_{L^\infty(\mathbb T)}=O(\sqrt D),
\qquad
|p_{m,D}|=O(\sqrt D)
\tag{30}
\]

for every Laurent coefficient.

Now prescribe target coefficients on both Vieta edges. For the strongest simple control, take

\[
\tau_D^+=\tau_D^-=1,
\qquad
\tau_{D-r}^+=\tau_{-D+r}^-=0
\quad(1\le r\le K).
\tag{31}
\]

Starting at frequency `D`, add a linear combination of `C_D,S_D` to set the `+D` and `-D` coefficients to one. Then, for `r=1,2,...,K`, add a linear combination

\[
\alpha_r C_{D-r}+\beta_r S_{D-r}
\tag{32}
\]

to set the two coefficients at `+(D-r)` and `-(D-r)` to their targets. Because (32) has degree exactly `D-r`, it never changes a coefficient fixed at an earlier step. Equations (14)--(15) make the two-by-two edge matrix

\[
\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\tag{33}
\]

so every step is exactly invertible with condition number independent of `D`.

Using (27), (30), and induction in `r` gives the crude but sufficient coefficient bound

\[
\boxed{
|\alpha_r|+|\beta_r|
\le (CD)^{C(r+1)},
\qquad 0\le r\le K.
}
\tag{34}
\]

The same construction can prescribe any target edge prefixes whose entries are `exp(O(K log D))`; bounded targets are more than enough for the Vieta application. Thus the vanishing choice (31) is not a special cancellation but one point in a large family of locally invisible Vieta states.

## 4. The total repair stays exponentially smaller than the XF-078 accuracy scale

Let

\[
Q_{D,K}(\theta)
:=B_D(\theta)-A_D(\theta)
\tag{35}
\]

be the sum of the `2(K+1)` Chebyshev corrections. On the real center interval, equations (19) and (34) give

\[
\begin{aligned}
\max_{j\le J}\|\partial_\theta^jQ_{D,K}\|_\infty
&\le
2^{-D}D^{C_J}
\sum_{r=0}^{K}
2^r(CD)^{C(r+1)}\\
&\le
\exp\!\left(
-(\log2)D+O_J(K\log D)+O_J(\log D)
\right).
\end{aligned}
\tag{36}
\]

If `K log D=o(D)`, this is `exp(-(log 2-o(1))D)`.

On the shrinking complex line (5), equation (25) inserts the additional factor `exp(O_J(D^(3/4)))`. Hence

\[
\boxed{
\max_{j\le J}
\sup_{(5)}
|\partial_\theta^jQ_{D,K}|
\le
\exp\!\left(
-(\log2)D
+O_J(K\log D)
+O_J(D^{3/4})
\right).
}
\tag{37}
\]

Under (2) the exponent is `-Theta(D)`, proving (6).

XF-078 already gives

\[
A_D(\theta)
=e^{i\theta/2}+O_J(e^{-c_JD})
\tag{38}
\]

on the center high line, while the true matched Gaussian quotient differs from the half-frequency wave there by the still smaller image term. Combining (37)--(38) shows that `B_D` is just as accurate a center-local matched surrogate at the scale relevant to the Xi construction.

At the actual Xi parameters,

\[
D=q^2,
\qquad
K\le Cq\log\log T,
\tag{39}
\]

so

\[
K\log D
=O(q\log q\log\log T)
=o(q^2)=o(D).
\tag{40}
\]

Thus the repair covers not merely a fixed number of low Vieta modes but the **entire growing source-visible range** used by XF-070--XF-071.

## 5. The repaired carrier can have zero Vieta resource through the whole source band

For `N=2D`, the centered XF-067 carrier has frequencies `D-r`, `0<=r<=N`, as in (7). Because (4) fixes the positive outer coefficient to one,

\[
E_r=(-1)^r b_{D-r,D}.
\tag{41}
\]

The negative outer condition in (4) simultaneously gives `E_N=1`, and the matching lower-edge zero conditions give `E_{N-r}=0` for `1<=r<=K`. Therefore (8) follows exactly.

Newton's identity

\[
rE_r
=\sum_{m=1}^r(-1)^{m-1}E_{r-m}P_m
\tag{42}
\]

then inductively yields (9). In particular, if the XF-070 weighted resource is restricted to the Vieta band `1<=m<=K`, then for this repaired surrogate

\[
\boxed{
\sum_{m=1}^{K}w_m|P_m|^2=0.
}
\tag{43}
\]

This should be compared directly with XF-080. The original explicit `A_D` has

\[
|P_1|\sim2D
\tag{44}
\]

and its `m=1` term alone has a nonvanishing normalized weighted cost in the XF-070 geometry. Yet `A_D` and `B_D` differ by `exp(-cD)` on the actual center Xi high line, with every fixed number of derivatives.

Therefore no stability implication of the form

\[
\text{center-local }C^J\text{ accuracy}
\quad\Longrightarrow\quad
\text{controlled XF-070 Vieta resource}
\tag{45}
\]

can hold for unrestricted `N+1`-mode trigonometric surrogates. The failure is not a bad constant in the explicit XF-078 approximation: the local restriction has an exponentially large coefficient nullspace, and the Vieta coordinates live precisely in directions that nullspace can change.

## 6. Stress tests and failure boundary

The result is deliberately **static**. The repaired `B_D` is not asserted to solve the Gaussian quotient drift equation, backward heat, or the exact periodic zero dynamics over a time interval. A dynamical residual small in the destination norm could remove much of the Chebyshev freedom. Consequently XF-081 rules out only source dictionaries based on frozen center-local function approximation plus coefficient conditioning; it does not rule out a heat-compatible surrogate theorem.

The construction also does not assert that the roots of `B_D` are real or bounded displacements of the arithmetic lattice. Conditions (4), (8), and (9) make its low Vieta data perfectly lattice-like and set the terminal coefficient exactly to one, but the uncontrolled middle coefficients may still place auxiliary roots off the unit circle. This is not a defect in the counterexample: it identifies exactly the additional information a root-faithful dictionary would have to supply. Local function accuracy and a long Vieta prefix do not supply it.

The shrinking imaginary height is load-bearing. On a fixed complex-height rectangle, the Chebyshev functions can grow exponentially fast enough to consume the `2^{-D}` gain. Thus XF-081 does not contradict XF-078's stronger fixed-rectangle approximation theorem. It says that **on the actual Xi high line**, where the source information is consumed, the coefficient nullspace remains exponentially invisible.

The prefix length condition `K log D=o(D)` is also genuine for this elementary construction. It comfortably includes the Mathia range `K=O(q log log T)`, `D=q^2`; no claim is made that all `Theta(D)` Vieta coefficients can be prescribed at negligible local cost.

Finally, (43) is not evidence that the true Xi transition state has zero weighted resource. It is the opposite: it shows that an arbitrary locally accurate surrogate can be made to report zero resource whether or not Xi has it. The repaired carrier is therefore a negative control against treating static approximation as a source-faithful encoding.

## 7. Prior-art and novelty boundary

Chebyshev polynomials as least-deviation polynomials, Remez-type inequalities, and the general phenomenon that a polynomial can be exponentially small on a proper interval or arc while having a prescribed leading coefficient are classical approximation theory. No novelty is claimed for that mechanism, for the identities of `T_n,U_n`, or for the triangular prescription of finitely many coefficients in isolation. A targeted prior-art audit found the expected Chebyshev/Remez and trigonometric-polynomial conditioning literature, not a de Bruijn--Newman or Vieta-flow theorem matching the present scaling.

The line-specific mathematical delta is the exact combination of that classical nullspace with the XF-067 centered Vieta dictionary and the XF-070--XF-071 Xi scales. Equations (37)--(43) show that the nullspace is large enough to prescribe **all Vieta modes through `O(q log log T)` while remaining `exp(-Theta(q^2))`-invisible on the actual Xi center high line**. That is precisely the range which a Gaussian-to-Vieta source theorem would otherwise try to infer from the local surrogate.

No external theorem is load-bearing for the derivation, so `SOURCES.md` is unchanged.

## 8. Consequence for `xi_flow`

XF-080 identified a conditioning failure of one canonical center-local approximant. XF-081 shows that replacing it by a better-conditioned static approximant does not close the dictionary: the coefficient state can be changed almost arbitrarily without changing the local function at the source accuracy scale. The problem is therefore **nonidentifiability**, not merely poor choice of approximation basis.

This removes one tempting continuation of the Gaussian/Vieta route. A future bridge cannot justify its Vieta state by saying only that an `N+1`-mode carrier approximates the Gaussian/Appell quotient on the safe center line and has acceptable outer coefficients or a controlled low prefix. It must select the carrier by an additional source-faithful principle that the Chebyshev nullspace cannot fake.

The cleanest surviving alternative is the one already suggested after XF-079--XF-080: avoid promoting the local quotient itself to a zero polynomial, and map a source-faithful object such as its logarithmic derivative directly into the one-center selector/weighted resource. A root-faithful or heat-residual-controlled finite carrier remains logically possible, but its extra constraint is now load-bearing and must be quantified in the exact XF-070 norm.

Nothing here proves that a hypothetical `Lambda>0` transition has nonzero guarded destination mass, so the separate transition-state gate remains unchanged.