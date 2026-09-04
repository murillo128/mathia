# ANF-030 — the Montgomery--Taylor extremizer forces Palm zero-set rigidity

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + DIFFRACTION-DUAL + RIGIDITY + NEGATIVE/OBSTRUCTION`. `ANF-020` turns the remaining universal-affine scalar problem into domination by the Montgomery--Taylor band budget

\[
\nu_{\rm MT}
=a_{\rm MT}\,\delta_0+a_{\rm MT}|h|\,dh,
\qquad
 a_{\rm MT}=C_{\rm MT}^{-1},
\]

and `ANF-023`--`ANF-029` test increasingly flexible stationary point-process candidates against that budget. The exact one-delta extremizer of Montgomery--Taylor / Carneiro--Chandee--Littmann--Milinovich gives a stronger structural test than the local cusp and reciprocal-spike filters used there.

There is an explicit continuous even spectrum `J_MT>=0`, supported in `[-1,1]`, whose spatial Fourier transform `R_MT=widehat J_MT` is nonnegative and satisfies

\[
\boxed{
\widehat J_{\rm MT}(0)=1,
\qquad
C(J_{\rm MT})=C_{\rm MT}.
}
\tag{1}
\]

Consequently

\[
\boxed{
\int J_{\rm MT}\,d\nu_{\rm MT}=1.
}
\tag{2}
\]

Now let `mu` be a full normalized diffraction measure whose inverse Fourier transform is a positive Palm correlation measure

\[
\eta=\delta_0+\eta^\circ,
\qquad \eta^\circ\ge0.
\tag{3}
\]

If `mu<=nu_MT` on `(-1,1)`, then Fourier duality and (1)--(2) give

\[
1+\int R_{\rm MT}(x)\,d\eta^\circ(x)
=
\int J_{\rm MT}\,d\mu
\le
\int J_{\rm MT}\,d\nu_{\rm MT}
=1.
\]

Since `R_MT>=0`, equality is forced throughout:

\[
\boxed{
R_{\rm MT}\,\eta^\circ=0.
}
\tag{4}
\]

Thus every stationary-process witness at the sharp Montgomery--Taylor budget must put **all off-diagonal Palm pair mass on the zero set of the exact Montgomery--Taylor extremizer**. Because that zero set is discrete, any candidate with a nonzero absolutely continuous Palm pair component is ruled out immediately.

This closes the entire open joint logarithmic-Gaussian mixture from `ANF-029`: arbitrary mixing over both variogram amplitude `c>0` and intensity `rho>0` cannot help. In fact every nondegenerate Gaussian Palm-lattice component already has strictly positive `J_MT`-energy above the sharp value `1`, independently of how its reciprocal spike is moved. If the family is enlarged to allow the singular endpoint `c=0`, domination forces all mixture mass onto that crystalline endpoint, where `ANF-022` rules out arbitrary scale mixing. The moving-soft-reciprocal branch is therefore closed.

## 1. The exact extremizer has a positive compact-band spectrum

Put

\[
\theta:=2^{-1/2}
\]

and define

\[
g(u)
:=
\frac{\cos(\sqrt2\,u)}{\sqrt2\sin\theta}
\,\mathbf 1_{[-1/2,1/2]}(u).
\tag{5}
\]

Because `|sqrt(2)u|<=theta<pi/2` on the support,

\[
\boxed{g(u)>0\quad (|u|<1/2),}
\tag{6}
\]

and direct integration gives

\[
\int_{-1/2}^{1/2}g(u)\,du=1.
\tag{7}
\]

Its Fourier transform in the Mathia convention is obtained by one elementary cosine integral:

\[
S(x):=\widehat g(x)
=
\frac{
\cos(\pi x)-\sqrt2\,\pi x\cot\theta\,\sin(\pi x)
}{1-2\pi^2x^2},
\tag{8}
\]

with the apparent poles at `x=+-1/(sqrt(2)pi)` removable. Therefore

\[
R_{\rm MT}(x):=S(x)^2
=
\frac{
\left(
\cos(\pi x)-\sqrt2\,\pi x\cot\theta\,\sin(\pi x)
\right)^2
}{(1-2\pi^2x^2)^2}.
\tag{9}
\]

Equation (9) is exactly the equality case in Corollary 14 of Carneiro--Chandee--Littmann--Milinovich. In particular `R_MT>=0`, `R_MT(0)=1`, and it is a nonzero entire function of exponential type `2pi`; hence its real zero set is discrete.

Define

\[
\boxed{J_{\rm MT}:=g*g.}
\tag{10}
\]

Then `J_MT` is continuous, even, nonnegative, supported in `[-1,1]`, and is strictly positive on `(-1,1)` by (6). Moreover

\[
\widehat J_{\rm MT}=S^2=R_{\rm MT},
\qquad
\widehat J_{\rm MT}(0)
=\left(\int g\right)^2
=1.
\tag{11}
\]

This explicit inverse transform is the load-bearing extra fact for the diffraction application: the classical one-delta extremizer is not merely nonnegative in physical space; its compact-band Fourier profile is also pointwise nonnegative.

## 2. Its BGSST cost is exactly the Montgomery--Taylor constant

For a nonnegative admissible spatial function `R` with Fourier transform `J` supported in `[-1,1]`, write the CCLM pair-correlation functional

\[
M(R)
=
\int_{\mathbb R}
R(x)
\left[1-\left(\frac{\sin\pi x}{\pi x}\right)^2\right]dx.
\tag{12}
\]

The Fourier transform of `sinc^2(x)` is `(1-|h|)_+`. Since `J_MT` is supported in `[-1,1]` and `R_MT(0)=int J_MT=1`, Parseval gives

\[
\begin{aligned}
M(R_{\rm MT})
&=J_{\rm MT}(0)
-\int_{-1}^{1}J_{\rm MT}(h)(1-|h|)\,dh\\
&=J_{\rm MT}(0)-1
+\int_{-1}^{1}|h|J_{\rm MT}(h)\,dh.
\end{aligned}
\tag{13}
\]

CCLM Corollary 14 gives equality for (9):

\[
M(R_{\rm MT})
=
2^{-1/2}\cot(2^{-1/2})-\frac12
=C_{\rm MT}-1.
\tag{14}
\]

Combining (13)--(14),

\[
\boxed{
C(J_{\rm MT})
:=J_{\rm MT}(0)
+\int_{-1}^{1}|h|J_{\rm MT}(h)\,dh
=C_{\rm MT}.
}
\tag{15}
\]

Together with (11), this proves (1). The target budget is calibrated exactly rather than approximately:

\[
\int J_{\rm MT}\,d\nu_{\rm MT}
=a_{\rm MT}C(J_{\rm MT})=1.
\tag{16}
\]

There is therefore **zero slack** for any positive off-diagonal contribution measured by `R_MT`.

## 3. A general Palm support theorem at the sharp budget

Suppose a candidate full diffraction `mu` has inverse Fourier transform represented by a positive normalized Palm correlation measure as in (3). This is the standard normalization used throughout `ANF-023`--`ANF-029`: the diagonal/self point contributes exactly `delta_0` in Palm space.

Because `J_MT` is continuous and supported in the tested band,

\[
\int J_{\rm MT}(h)\,d\mu(h)
=
\int R_{\rm MT}(x)\,d\eta(x).
\tag{17}
\]

Using (3), (11), and nonnegativity,

\[
\int J_{\rm MT}\,d\mu
=
1+\int R_{\rm MT}(x)\,d\eta^\circ(x)
\ge1.
\tag{18}
\]

If `mu<=nu_MT` on `(-1,1)`, then `J_MT>=0` and (16) give the opposite inequality

\[
\int J_{\rm MT}\,d\mu\le1.
\tag{19}
\]

Hence equality holds in (18), proving (4). In particular,

\[
\boxed{
\operatorname{supp}\eta^\circ
\subseteq
Z_{\rm MT}:=\{x\in\mathbb R:R_{\rm MT}(x)=0\}
}
\tag{20}
\]

in the measure-theoretic sense.

Since `R_MT` is a nonzero entire function, `Z_MT` is discrete. Therefore any candidate for which `eta^circ` has a nonzero absolutely continuous component is impossible. More generally it is enough that `eta^circ` assign positive mass to any open interval on which `R_MT>0`.

This is qualitatively stronger than an infrared or reciprocal-frequency test. It constrains the **entire Palm pair measure at once** through a sharp equality case inherited from the Montgomery--Taylor extremal problem.

## 4. Arbitrary joint logarithmic-Gaussian mixtures are impossible

For the logarithmic stationary-increment Gaussian Palm lattice of `ANF-028`, after dilation to intensity `rho>0`, the expected Palm measure is

\[
\eta_{c,\rho}
=
\delta_0+
\sum_{n\ne0}
\operatorname{Law}\left(
\frac{n+B_n^{(c)}}{\rho}
\right),
\tag{21}
\]

where

\[
B_n^{(c)}\sim
N\!\left(0,c\log(1+n^2)\right)
\qquad(c>0).
\tag{22}
\]

Its Fourier transform is precisely the full normalized diffraction used in `ANF-028`--`ANF-029`,

\[
\mu_{c,\rho}
=
\rho\delta_0+S_c(h/\rho)\,dh.
\tag{23}
\]

Apply (17) directly. Already the `n=1` term gives

\[
\int J_{\rm MT}\,d\mu_{c,\rho}
\ge
1+
\mathbb E\,
R_{\rm MT}\!\left(\frac{1+B_1^{(c)}}{\rho}\right).
\tag{24}
\]

For every `c>0`, the random variable in (24) has a Gaussian density that is strictly positive on all of `R`. Since `R_MT` is continuous, nonnegative, and `R_MT(0)=1`,

\[
\boxed{
\mathbb E\,
R_{\rm MT}\!\left(\frac{1+B_1^{(c)}}{\rho}\right)>0
\qquad(c>0,\ \rho>0).
}
\tag{25}
\]

Thus every component has strict energy

\[
\boxed{
\int J_{\rm MT}\,d\mu_{c,\rho}>1.
}
\tag{26}
\]

Now let `Pi` be any probability law on `(c,rho) in (0,infinity)^2` for which the mixed diffraction

\[
\overline\mu_\Pi
=
\int\mu_{c,\rho}\,d\Pi(c,\rho)
\tag{27}
\]

is locally finite. Tonelli applies because all terms are nonnegative. Equations (24)--(26) imply

\[
\int J_{\rm MT}\,d\overline\mu_\Pi
>1,
\tag{28}
\]

whereas domination by `nu_MT` would force the left side to be at most `1`. Therefore

\[
\boxed{
\overline\mu_\Pi\not\le\nu_{\rm MT}
\quad\text{for every joint probability law }\Pi
\text{ on }(0,\infty)^2.
}
\tag{29}
\]

The conclusion is independent of the reciprocal-spike location. Varying `rho` may smear the finite-frequency feature that powered `ANF-028`--`ANF-029`, but Gaussian pair smearing itself is fatal because the sharp extremizer has no positive-energy slack.

## 5. The singular zero-noise endpoint reduces to the lattice class already killed in ANF-022

The same argument identifies exactly what happens if the parameter family is closed by allowing `c=0`. In that case `B_n^{(0)}=0` and the component is the deterministic lattice of intensity `rho`, with diffraction

\[
\mu_{0,\rho}
=
\rho\sum_{k\in\mathbb Z}\delta_{k\rho}.
\tag{30}
\]

For every `c>=0`, positivity of `R_MT` gives

\[
\int J_{\rm MT}\,d\mu_{c,\rho}\ge1,
\tag{31}
\]

with strict inequality for every `c>0`. Hence any mixed law on `[0,infinity) times (0,infinity)` whose diffraction were dominated by `nu_MT` would have to put zero mass on `c>0`; otherwise its `J_MT` integral would exceed the exact target value `1`.

It would therefore reduce entirely to a scale mixture of the lattice measures (30). `ANF-022` proves that **no probability mixture of those lattice diffractions can be dominated by `nu_MT`**. Consequently the logarithmic-Gaussian Palm-lattice route remains closed even after adjoining its crystalline zero-noise boundary.

This also clarifies the relation with `ANF-027`. One must distinguish an actual mixture on the closed parameter family from a more singular weak-limit procedure in which parameters themselves escape every compact set. The theorem above closes the former exactly. Any proposed escaping-parameter closure must be analyzed as a new limiting diffraction object rather than relabeled as a joint `(c,rho)` mixture.

## 6. Broader consequence for stationary diffraction candidates

The proof did not use the logarithmic form of the Gaussian variogram except to guarantee a nondegenerate continuous Palm displacement. Equation (20) therefore applies to any stationary point-process candidate with a positive Palm correlation representation.

In particular, any candidate with a diffuse off-diagonal Palm pair density is excluded at the sharp Montgomery--Taylor budget. This covers, at the structural level, the nondegenerate Gaussian perturbations studied in `ANF-025`--`ANF-029`, nonlattice renewal-type candidates such as those filtered in `ANF-024`, and the usual absolutely continuous pair-correlation component of determinantal/random-matrix processes from `ANF-020`--`ANF-021`. Their earlier local or model-specific obstructions remain correct, but the extremal-equality argument explains a common reason that all of them fail.

The surviving stationary-process geometry is therefore crystalline in a much stricter sense than “hyperuniform”: its entire off-diagonal Palm pair measure must live on the discrete zero set `Z_MT`. It is not enough to suppress the structure factor near the origin or to smear Bragg peaks while keeping the right slope.

This does **not** yet prove that `K cap {mu:mu<=nu_MT}` is empty. The closed convex finite-configuration body in `ANF-020` is larger than the class of full stationary diffractions for which a positive Palm inverse transform has been identified, and weak limits can lose a direct fixed-parameter Palm representation. The universal scalar question therefore remains open.

## 7. Prior-art and novelty boundary

The one-delta extremal theorem and the explicit equality function (9) are classical results of Montgomery--Taylor and, in the form used here, Corollary 14 of Carneiro--Chandee--Littmann--Milinovich, already anchored in `SOURCES.md`. The factorization (5)--(10) follows by an elementary Fourier transform of a truncated cosine and makes the positivity of the compact-band spectrum explicit. Palm/diffraction duality for the correlated Gaussian lattice is already the load-bearing point-process input of `ANF-025`--`ANF-029`.

A targeted check of perturbed-lattice/paracrystal diffraction and the existing Mathia structure-factor sources did not locate the support-rigidity consequence (20) or its use to close arbitrary joint log-Gaussian amplitude/intensity mixtures at the Montgomery--Taylor budget. No publication-level novelty claim is made. No `SOURCES.md` change is required because every external premise used here already has a durable source anchor.

## 8. Evidence boundary and next decisive test

The exact theorem is (20) for candidates possessing a positive normalized Palm correlation measure, together with the joint-mixture no-go (29). It does not identify all elements of the abstract convex diffraction body `K`, and it does not by itself rule out singular weak limits whose parameter laws are not tight enough to converge to an honest mixture on the closed `(c,rho)` parameter space.

The next structural question is now sharper than the moving-soft-reciprocal optimization left by `ANF-029`:

\[
\boxed{
\text{Can any positive-density stationary/Palm configuration have all pair differences in }Z_{\rm MT}?
}
\tag{32}
\]

For a deterministic infinite configuration this asks for an additive difference set contained in the real zeros of the explicit sine-type function (8). A proof that `Z_MT` contains no positive-density difference set would eliminate the entire stationary-process realization route, not merely Gaussian perturbations. Conversely, an explicit positive-density configuration with difference support in `Z_MT` would be a genuinely new survivor and should then be tested directly against the full band order `mu<=nu_MT`.

For the abstract `K` problem, the decisive audit is to determine whether every dominated weak-* witness can be approximated or represented strongly enough that the extremal equality (20) survives as a positive correlation measure statement. That is the remaining gap between the new Palm rigidity and a complete universal-affine scalar no-go.