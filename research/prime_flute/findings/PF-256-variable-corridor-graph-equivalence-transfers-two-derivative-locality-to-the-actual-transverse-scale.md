# PF-256 — variable-corridor graph equivalence transfers two-derivative locality to the actual transverse scale

**Status:** `EXACT-DERIVED + OPERATOR-DOMAIN-EQUIVALENCE + TWO-DERIVATIVE-SPECTRAL-BRIDGE + POSITIVE/ROUTE-NARROWING`.

[[research/prime_flute/findings/PF-233-variable-width-diagonal-corridor-has-exact-operator-valued-transfer-law|PF-233]] proves the form comparison `T_a \asymp s^2A` for the exact variable-width diagonal corridor, but [[research/prime_flute/findings/PF-255-hypercycle-compactification-transport-is-a-parity-local-flow-with-a-two-derivative-leakage-bound|PF-255]] correctly leaves open whether that form comparison is strong enough to transport spectral off-diagonal locality from the fixed-axis operator `A` to the actual corridor operator `K_a=T_a^{1/2}`. Form order alone cannot do this.

For the canonical PF-231/PF-233 hypercycle width there is, however, additional regularity that was not spent in the form estimate. Normalize

\[
q(\theta):=\frac{a(\theta)}s,
\qquad
P_a:=s^{-2}T_a,
\qquad
A=-\partial_\theta^2+\csc^2\theta.
\]

The exact hypercycle formulas imply that `q` is uniformly bounded away from zero and has uniformly bounded first two derivatives on the canonical tail. Expanding PF-233's transformed form then gives, on the Friedrichs core,

\[
\boxed{
P_a
=q^2A-2qq'\partial_\theta
-\frac12qq''-\frac14(q')^2.
}
\]

This upgrades the form comparison to a scale-uniform **operator graph comparison**:

\[
\boxed{
\operatorname{Dom}(P_a)=\operatorname{Dom}(A),
\qquad
C^{-1}\|Ay\|\le \|P_ay\|\le C\|Ay\|,
}
\]

with one constant after a finite canonical tail. Equivalently,

\[
P_aA^{-1},\quad A^{-1}P_a,\quad AP_a^{-1},\quad P_a^{-1}A
\]

all extend boundedly with uniform norms.

That operator-domain statement has an immediate spectral consequence. If `K_0=A^{1/2}` and `\widehat K_a=P_a^{1/2}=s^{-1}K_a`, then for `0<M<N`,

\[
\boxed{
\|\mathbf1_{[0,M]}(K_0)\mathbf1_{[N,\infty)}(\widehat K_a)\|
+\|\mathbf1_{[0,M]}(\widehat K_a)\mathbf1_{[N,\infty)}(K_0)\|
\le C\left(\frac MN\right)^2.
}
\]

Thus the actual transverse change of spectral scale cannot itself realize the arbitrary high-to-fixed-low rotation from PF-244. More generally, every bounded transport `W` that is graph-local through two `A^{1/2}` derivatives,

\[
AWA^{-1},\qquad A^{-1}WA\in\mathcal B,
\]

is graph-local through two `K_a` derivatives as well:

\[
T_aWT_a^{-1},\qquad T_a^{-1}WT_a\in\mathcal B
\]

uniformly on the canonical tail.

Applying this to PF-255's hypercycle half-density flow `V_c` and its scalar-trace/physical-density multipliers gives the actual-corridor estimate

\[
\boxed{
\|E^{(a)}_{\le M}V_cE^{(a)}_{\ge N}\|
\le C e^{6|c|}\left(\frac MN\right)^2,
}
\]

where `E^{(a)}` denotes the spectral projections of `K_a`. Consequently, for every fixed positive propagation distance `d`, every `0\le R\le2`, and every `Z>0`,

\[
\boxed{
K_ae^{-dK_a}V_cK_a^R\mathbf1_{(Z,\infty)}(K_a)\in\mathcal B
}
\]

with a tail bound of order `Z^{R-2}` for `R<2`. The PF-255 supercritical window `1<R<2` therefore survives the passage from the fixed-axis `A` modes to the actual variable-corridor `K_a` modes **without losing derivative order**.

This is a real closure of one branch of the accepted critical-Jacobi clue, but it is not the missing Robin theorem. The fixed-axis actual seam still has the critical `A^{-1/2}LA^{-1/2}` Jacobi edge, and PF-254's polar factor for `K_a^{-1/2}(Q_w^{\rm act})^{1/2}` is not shown here to satisfy either of the graph-locality hypotheses above. What is removed is the possibility that the already-controlled hypercycle transport becomes catastrophically nonlocal merely because the physical corridor uses `T_a` instead of `s^2A`.

## Claim

Let `a=a_s` be the exact PF-231/PF-233 canonical trimmed-corridor width

\[
a(\theta)
=s-f_{\rho_1}(\theta)-f_{\rho_2}(\theta),
\qquad
f_\rho(\theta)=\operatorname{arsinh}(\sinh\rho\,\sin\theta),
\tag{1}
\]

on a tail on which

\[
(1-\eta)s\le a\le s,
\qquad \eta\le\eta_*<1,
\qquad \rho_i=O(s).
\tag{2}
\]

Put

\[
q=a/s,
\qquad
P_a=s^{-2}T_a,
\qquad
K_0=A^{1/2},
\qquad
\widehat K_a=P_a^{1/2}=s^{-1}K_a.
\tag{3}
\]

Then there are tail-uniform constants `C_j<\infty` and `\mu>0` such that:

1. `q\ge1-\eta_*>0` and
   \[
   \|q\|_\infty+\|q'\|_\infty+\|q''\|_\infty\le C_0;
   \tag{4}
   \]
2. on `C_c^\infty(0,\pi)`, and hence distributionally on the common operator domain,
   \[
   \boxed{
   P_a
   =q^2A-2qq'\partial_\theta
   -\frac12qq''-\frac14(q')^2;
   }
   \tag{5}
   \]
3. the Friedrichs operators have the same domain and uniformly equivalent graph norms,
   \[
   \boxed{
   \operatorname{Dom}(P_a)=\operatorname{Dom}(A),
   \qquad
   C_1^{-1}\|Ay\|\le\|P_ay\|\le C_1\|Ay\|;
   }
   \tag{6}
   \]
4. the four relative graph maps
   \[
   P_aA^{-1},\quad A^{-1}P_a,\quad AP_a^{-1},\quad P_a^{-1}A
   \tag{7}
   \]
   have uniformly bounded extensions on `L^2((0,\pi),d\theta)`;
5. for `0<M<N`, with
   \[
   E^0_{\le M}=\mathbf1_{[0,M]}(K_0),
   \qquad
   \widehat E^a_{\ge N}=\mathbf1_{[N,\infty)}(\widehat K_a),
   \tag{8}
   \]
   and analogously for the opposite spectral cuts,
   \[
   \boxed{
   \|E^0_{\le M}\widehat E^a_{\ge N}\|
   \le C_2(M/N)^2,
   \qquad
   \|\widehat E^a_{\le M}E^0_{\ge N}\|
   \le C_2(M/N)^2;
   }
   \tag{9}
   \]
6. if a bounded operator `W` satisfies
   \[
   AWA^{-1},\quad A^{-1}WA\in\mathcal B,
   \tag{10}
   \]
   then
   \[
   \boxed{
   T_aWT_a^{-1},\quad T_a^{-1}WT_a\in\mathcal B
   }
   \tag{11}
   \]
   with bounds controlled by (7) and (10);
7. for PF-255's `V_c`,
   \[
   \boxed{
   \|\mathbf1_{[0,M]}(K_a)V_c\mathbf1_{[N,\infty)}(K_a)\|
   \le C_3e^{6|c|}(M/N)^2;
   }
   \tag{12}
   \]
   and, for `d>0`, `0\le R\le2`, `Z>0`,
   \[
   \boxed{
   \|K_ae^{-dK_a}V_cK_a^R\mathbf1_{(Z,\infty)}(K_a)\|
   \le
   C_3e^{6|c|}
   \sup_{\lambda\ge0}\lambda^3e^{-d\lambda}
   Z^{R-2}.
   }
   \tag{13}
   \]

The same transfer applies to the `W^{2,\infty}` scalar-trace and physical-density multipliers already isolated in PF-255. No statement is made here for the unresolved intrinsic seam square root or PF-254 polar factor.

## 1. The canonical normalized width is uniformly `W^{2,\infty}`

Write `w=\sinh\rho`. From (1),

\[
f_\rho'(\theta)
=\frac{w\cos\theta}{\sqrt{1+w^2\sin^2\theta}},
\tag{14}
\]

and one more derivative simplifies exactly to

\[
\boxed{
 f_\rho''(\theta)
 =-\frac{w(1+w^2)\sin\theta}
 {(1+w^2\sin^2\theta)^{3/2}}.
}
\tag{15}
\]

Hence

\[
\|f_\rho'\|_\infty\le w,
\qquad
\|f_\rho''\|_\infty\le w(1+w^2).
\tag{16}
\]

PF-231 gives `\rho_i=O(s)` on the canonical tail. Therefore `w_i=\sinh\rho_i=O(s)`, and division of (1) by `s` gives

\[
\|q'\|_\infty
\le\frac{w_1+w_2}{s}=O(1),
\qquad
\|q''\|_\infty
\le\frac{w_1(1+w_1^2)+w_2(1+w_2^2)}s=O(1).
\tag{17}
\]

Together with (2), this proves (4). Notice that this does **not** assume `q\to1`: PF-233 explicitly allows an order-one relative width profile. The argument spends regularity, not smallness.

## 2. The PF-233 form has an exact second-order differential expression

PF-233 gives, after `y=a^{-1/2}v`,

\[
\tau_a[y]
=\int_0^\pi a^2
\left(
\left|y'+\frac{a'}{2a}y\right|^2
+\csc^2\theta\,|y|^2
\right)d\theta.
\tag{18}
\]

Since `a=sq`, division by `s^2` gives the closed form of `P_a`:

\[
p_a[y]
=\int_0^\pi q^2
\left(
\left|y'+\frac{q'}{2q}y\right|^2
+\csc^2\theta\,|y|^2
\right)d\theta.
\tag{19}
\]

Integrating by parts on the Friedrichs core yields

\[
P_ay
=-q^2y''-2qq'y'
+\left(
q^2\csc^2\theta
-\frac12qq''-\frac14(q')^2
\right)y,
\tag{20}
\]

which is (5). The inverse-square endpoint term is exactly the same `q^2\csc^2\theta` principal potential that appears when `q^2A` is expanded; all new terms contain only bounded coefficients from (4).

## 3. Form comparability plus the exact expression gives operator-domain equality

Let `\alpha=(1+\sqrt5)/2`. PF-247 gives `A\ge\alpha^2`, and PF-255 records for `y\in\operatorname{Dom}A`

\[
\|y\|\le\alpha^{-2}\|Ay\|,
\qquad
\|y'\|\le\alpha^{-1}\|Ay\|.
\tag{21}
\]

Using (5), (4), and (21), every `y\in\operatorname{Dom}A` satisfies

\[
\|P_ay\|
\le C\|Ay\|.
\tag{22}
\]

The right side of (5) is in `L^2`, and the core identity extends through the closed form, so `\operatorname{Dom}A\subseteq\operatorname{Dom}P_a`.

For the converse, PF-233's lower form estimate divided by `s^2` gives a tail-uniform `\mu>0` with

\[
P_a\ge_{\rm form}\mu A\ge\mu\alpha^2I.
\tag{23}
\]

If `y\in\operatorname{Dom}P_a`, then `y` lies in the common form domain and

\[
\|y\|
\le(\mu\alpha^2)^{-1}\|P_ay\|,
\tag{24}
\]

while

\[
\|y'\|^2
\le \langle y,Ay\rangle_{\rm form}
\le\mu^{-1}\langle y,P_ay\rangle
\le\mu^{-1}\|y\|\|P_ay\|.
\tag{25}
\]

Thus

\[
\|y'\|\le(\mu\alpha)^{-1}\|P_ay\|.
\tag{26}
\]

Solving (5) distributionally for `Ay` gives

\[
Ay
=q^{-2}P_ay
+2\frac{q'}q y'
+\left(
\frac{q''}{2q}
+\frac{(q')^2}{4q^2}
\right)y.
\tag{27}
\]

Every term on the right is in `L^2` by (4), (24), and (26). Since `y` is already in the Friedrichs form domain, the form characterization of `A` now gives `y\in\operatorname{Dom}A`, and (27) gives

\[
\|Ay\|\le C\|P_ay\|.
\tag{28}
\]

Equations (22) and (28) prove (6). They also show directly that `P_aA^{-1}` and `AP_a^{-1}` are uniformly bounded. Taking adjoints gives the bounded extensions of `A^{-1}P_a` and `P_a^{-1}A`, proving (7).

This is the step unavailable from quadratic-form order alone: it uses the canonical width's explicit two-derivative coefficient control.

## 4. The fixed-axis and variable-corridor spectral bases have an order-two leakage barrier

Let `E^0_{\le M}` and `\widehat E^a_{\ge N}` be as in (8). On spectral truncations, insert the identity in the form

\[
I=A(A^{-1}P_a)P_a^{-1}.
\tag{29}
\]

Using (7),

\[
\begin{aligned}
\|E^0_{\le M}\widehat E^a_{\ge N}\|
&\le
\|E^0_{\le M}A\|
\,\|A^{-1}P_a\|
\,\|P_a^{-1}\widehat E^a_{\ge N}\|\\
&\le C M^2N^{-2}.
\end{aligned}
\tag{30}
\]

Similarly, using

\[
I=P_a(P_a^{-1}A)A^{-1},
\tag{31}
\]

gives the reverse estimate in (9). Closure removes the temporary spectral truncations.

Because `\widehat K_a=s^{-1}K_a`, (9) compares the physically correct scaled bands: a `K_0` frequency `N` corresponds to a `K_a` frequency of order `sN`. The result does not say that the two eigenbases are close coefficient-by-coefficient; it says that their separated high/low conversion has two derivatives of protection.

## 5. Two-derivative graph locality transfers without loss

Suppose (10) holds. Then the four graph maps from (7) factor the corresponding `P_a` conjugations exactly:

\[
P_aWP_a^{-1}
=(P_aA^{-1})(AWA^{-1})(AP_a^{-1}),
\tag{32}
\]

and

\[
P_a^{-1}WP_a
=(P_a^{-1}A)(A^{-1}WA)(A^{-1}P_a).
\tag{33}
\]

Both are uniformly bounded. Since `T_a=s^2P_a`, the scalar scale cancels from the same conjugations, proving (11).

In particular, if `E^{(a)}_{\le M}=\mathbf1_{[0,M]}(K_a)`, then from the second operator in (11),

\[
\begin{aligned}
\|E^{(a)}_{\le M}WE^{(a)}_{\ge N}\|
&\le
M^2\|T_a^{-1}WT_a\|N^{-2},
\end{aligned}
\tag{34}
\]

which is the actual-`K_a` order-two high-to-low bound.

PF-255 proves both `AVA^{-1}` and `A^{-1}V_cA` bounded by `e^{6|c|}`. Substitution into (32)--(34) gives (12), up to the tail-uniform graph-equivalence constants. The same factorization applies to PF-255's width-dependent scalar-trace and physical-density multipliers because their coefficients and inverses are uniformly `W^{2,\infty}` and PF-255 already proves their `A`-graph boundedness.

## 6. Positive separation preserves the same `R\le2` window in `K_a` modes

Put

\[
B_a:=T_a^{-1}V_cT_a.
\tag{35}
\]

By (11), `\|B_a\|\le C e^{6|c|}`. Hence

\[
V_c=T_aB_aT_a^{-1}
\]

and, because `T_a=K_a^2`,

\[
K_ae^{-dK_a}V_cK_a^R\mathbf1_{(Z,\infty)}(K_a)
=K_a^3e^{-dK_a}
B_aK_a^{R-2}\mathbf1_{(Z,\infty)}(K_a).
\tag{36}
\]

For `0\le R\le2`, the two outer factors are bounded and

\[
\|K_a^{R-2}\mathbf1_{(Z,\infty)}(K_a)\|
\le Z^{R-2}.
\tag{37}
\]

This proves (13). In particular every `1<R<2` required qualitatively by PF-243 remains available after the exact `A\leftrightarrow T_a` transfer for this already-controlled geometric transport.

## 7. Prior-art and novelty audit

Operator-domain descriptions for semibounded singular Sturm--Liouville Friedrichs extensions are classical. A representative reference is S. Yao, J. Sun, A. Zettl, *The Sturm-Liouville Friedrichs extension*, Applications of Mathematics **60** (2015), 299--320, DOI `10.1007/s10492-015-0097-3`. Relative boundedness and compactness of perturbations of second-order differential operators are likewise classical; see T. G. Anderson, D. B. Hinton, *Relative boundedness and compactness theory for second-order differential operators*, Journal of Inequalities and Applications **1** (1997), 375--400.

Those sources are prior-art context rather than imported proof steps here. Equations (20)--(28) establish the needed domain and graph estimates directly from the exact PF-233 form, PF-231's canonical hypercycle coefficients, and the already-persisted inverse-square `A` bounds. A structure-directed literature search did not identify the PF-specific conclusion (9)--(13): the scale-normalized variable corridor has a two-derivative spectral change-of-basis barrier, and this transfers PF-255's hypercycle locality to the actual `K_a` spectral basis. No novelty is claimed for general Sturm--Liouville domain theory, graph norms, relative boundedness, or the spectral theorem.

## 8. Adversarial checks and boundaries

1. **The result uses more than form order.** If only `cA\le P\le CA` were known as quadratic forms, (6), (7), and (9) would not follow. The proof depends essentially on the exact differential expression and uniform `q''` control.
2. **No small-profile assumption.** The canonical ratio `q=a/s` need not converge to `1`; only a positive lower bound and uniform first two derivatives are used. This is consistent with PF-233's order-one width-profile warning.
3. **Scaled cross-basis comparison.** The direct `A`/`T_a` projection estimate must compare `K_0` with `s^{-1}K_a`. Omitting the factor `s^{-1}` would compare different physical frequency scales.
4. **No arbitrary polar-factor theorem.** Equations (11)--(13) apply only to operators already known to be two-derivative graph-local for `A`. PF-254's residual `U_w` has not been shown to satisfy that premise.
5. **No automatic transfer of PF-253.** The sharp fractional kernel of `J_\varepsilon^\sigma` is not promoted to a `K_a` theorem merely from (6). Its use in the actual Robin factor still requires an exact operator dictionary for the fixed-axis seam/relative variable and control of the polar orientation.
6. **Canonical tail only.** Uniform constants use the PF-231/PF-233 tail bounds `\eta\le\eta_*<1` and `\rho_i=O(s)`. A degenerate trimmed corridor with `q\downarrow0` is outside the theorem.
7. **No physical/global closure.** The result does not prove the full PF-243 Robin-Poisson estimate, physical `P/H` recoupling, finite-pant completion, global weak-`S_1` reassembly, scattering/determinant control, zeta-zero statements, or RH.

## Consequences for the research line

PF-255's last explicit `A\to T_a` locality caveat is now closed for every factor that is already graph-local through two `A^{1/2}` derivatives. The variable-width corridor changes the transverse operator substantially enough that form comparison was insufficient, but its exact hypercycle coefficient regularity forces the two Friedrichs operators to have the same operator domain with uniformly equivalent graph norms after the natural `s^2` scaling. Therefore neither the `A\leftrightarrow T_a` basis change nor the PF-235/PF-255 hypercycle coordinate/density transport can be the PF-244-style catastrophic mixer.

The accepted critical-Jacobi route narrows to the genuinely singular noncommutative object: the **fixed-axis actual seam relative to `K_a` and the polar factor of its normalized square root**. The next theorem must show that this seam/Jacobi functional calculus itself satisfies enough `K_a` high-to-low control for some `R>1`, or produce an actual-seam sequence showing that it does not.