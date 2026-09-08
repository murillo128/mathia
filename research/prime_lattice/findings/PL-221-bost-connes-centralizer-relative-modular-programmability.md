# PL-221 — Bost–Connes commuting same-sector modular data is exactly diagonal and spectrally programmable

## Claim

The same-sector relative-modular escape left open by `PL-213`, `PL-215`, `PL-216`, and `PL-220` has an exact negative classification for **normal states that commute with the canonical high-temperature KMS state**.

Fix

\[
0<\beta\le1,
\]

let `phi_beta` be the unique rational Bost--Connes `KMS_beta` state, let

\[
(M_\beta,\widetilde\phi_\beta)
=
(\pi_\beta(\mathcal A_{BC})'',\widetilde\phi_\beta)
\]

be its GNS von Neumann algebra and faithful normal vector state, and let

\[
\mathcal D=C^*(\mathbb Q/\mathbb Z)\cong C(\widehat{\mathbb Z})
\]

be the cyclotomic diagonal from `PL-219`. Then the modular centralizer of the KMS state is exactly the weak diagonal:

\[
\boxed{
M_\beta^{\widetilde\phi_\beta}
=
\pi_\beta(\mathcal D)''.
}
\]

Consequently the Pedersen--Takesaki Radon--Nikodym theorem classifies every normal state `psi` that commutes with `widetilde phi_beta`: its Radon--Nikodym density is a positive self-adjoint operator affiliated with the **abelian** algebra `pi_beta(D)''`. In the faithful bounded case, for every positive invertible

\[
h\in\pi_\beta(\mathcal D)'',
\]

the normalized state

\[
\psi_h(x)
=
\frac{\widetilde\phi_\beta(h^{1/2}xh^{1/2})}
{\widetilde\phi_\beta(h)}
\]

has Connes cocycle

\[
\boxed{
[D\psi_h:D\widetilde\phi_\beta]_t
=
\left(\frac{h}{\widetilde\phi_\beta(h)}\right)^{it}.
}
\]

Thus the corresponding relative modular generator is simply

\[
K_h
=
\log h-\log\widetilde\phi_\beta(h),
\]

an arbitrary diagonal observable subject only to normalization. Its spectrum is not forced by the prime logarithms or by the Riemann zero divisor.

A one-prime matched control already makes the programmability explicit. Let `e_p` be the clopen diagonal projection of the event `v_p>=1`. Under the canonical high-temperature diagonal measure,

\[
\widetilde\phi_\beta(e_p)=p^{-\beta}.
\]

For arbitrary `a,b>0`, set

\[
h=a e_p+b(1-e_p).
\]

Then `K_h` has two spectral values whose gap is

\[
\boxed{\log a-\log b=\log(a/b),}
\]

which can be prescribed arbitrarily while the underlying Bost--Connes system, prime `p`, temperature `beta`, and Riemann zeta function are held fixed. Finite clopen partitions give the corresponding finite-level spectral programmability.

Therefore **commuting same-sector Connes cocycles and relative modular Hamiltonians do not provide an RH-sensitive invariant**. The negative is stronger than the diagonal product-measure tangent control in `PL-216`: it classifies the entire Pedersen--Takesaki commuting normal-state sector of the high-temperature factor, not only primewise product perturbations. A surviving Bost--Connes route must use genuinely noncommuting same-sector states/weights, unbounded data not reducible to a centralizer density, or a global trace/positivity construction that imposes an independently arithmetic relation among prime channels.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE/CONTROL + PRIOR-ART-AUDITED + NO-NOVELTY-CLAIM`.

The operator-algebraic ingredients are classical: the KMS/modular identification, the Pedersen--Takesaki Radon--Nikodym theorem, and the Bost--Connes KMS structure. The line-specific content is the exact identification of the high-temperature centralizer with the weak cyclotomic diagonal using the dense prime-gauge flow from `PL-219`, followed by the explicit one-prime programmability control. No novelty is claimed for modular theory or for the Bost--Connes system.

## 1. The KMS modular flow has the same fixed points as physical time

A `KMS_beta` GNS vector is modular. With the standard KMS convention, the modular automorphism group of the normal extension satisfies

\[
\sigma_t^{\widetilde\phi_\beta}(\pi_\beta(a))
=
\pi_\beta(\sigma_{-\beta t}(a)),
\qquad a\in\mathcal A_{BC}.
\]

The sign convention is irrelevant here: multiplication of the time parameter by the nonzero scalar `-beta` does not change the fixed-point algebra. Hence

\[
M_\beta^{\widetilde\phi_\beta}
=
M_\beta^{\sigma},
\]

where the right side denotes the fixed points of the physical Bost--Connes time flow in the GNS von Neumann algebra.

This is the standard KMS--Tomita--Takesaki identification. A classical source is Masamichi Takesaki, *Tomita's Theory of Modular Hilbert Algebras and its Applications*, Lecture Notes in Mathematics 128, Springer, 1970, especially the chapter on the modular automorphism group and the Kubo--Martin--Schwinger boundary condition. Huzihiro Araki's review “On the Kubo--Martin--Schwinger Boundary Condition,” *Progress of Theoretical Physics Supplement* **64** (1978), 12--20, DOI `10.1143/PTPS.64.12`, gives the same bridge in equilibrium language.

No complex zeta variable is introduced in this step. `beta` remains a real inverse temperature, and modular time is only a rescaling of the already-defined physical dynamics.

## 2. The dense prime-gauge flow identifies the centralizer with the weak diagonal

`PL-219` constructs the compact prime-gauge group

\[
G=\widehat{\mathbb Q_+^\times}
\cong\mathbb T^{\mathcal P}
\]

acting by

\[
\gamma_z(e(r))=e(r),
\qquad
\gamma_z(\mu_n)=z(n)\mu_n,
\]

and proves two facts on the `C*`-algebra:

\[
\overline{\{z(t):t\in\mathbb R\}}=G,
\qquad z_p(t)=p^{it},
\]

and

\[
\mathcal A_{BC}^{G}=\mathcal D.
\]

Because `phi_beta` is gauge invariant, the gauge action is unitarily implemented in the GNS representation. For `z in G`, define on the dense GNS subspace

\[
U_z\pi_\beta(a)\Omega_\beta
=
\pi_\beta(\gamma_z(a))\Omega_\beta.
\]

Gauge invariance makes this isometric, and norm continuity of `gamma` implies strong continuity of `z -> U_z`. Therefore

\[
\overline\gamma_z(x)=U_zxU_z^*,
\qquad x\in M_\beta,
\]

defines a normal action of the compact group `G` on `M_beta`.

If `x` is fixed by physical time, then it is fixed by the dense subgroup `z(t)`. Strong continuity in `z` gives

\[
x\in M_\beta^G.
\]

The converse is immediate, so

\[
M_\beta^{\sigma}=M_\beta^G.
\]

It remains to identify the latter algebra. Haar averaging gives the normal conditional expectation

\[
\overline E_G:M_\beta\to M_\beta^G.
\]

On the norm-dense represented `C*`-algebra it agrees with the expectation from `PL-219`:

\[
\overline E_G(\pi_\beta(a))
=
\pi_\beta(E_G(a)),
\qquad E_G(a)\in\mathcal D.
\]

Take `x in M_beta^G` and an ultraweakly convergent bounded net `pi_beta(a_i) -> x`. Normality gives

\[
\pi_\beta(E_G(a_i))
=
\overline E_G(\pi_\beta(a_i))
\longrightarrow
\overline E_G(x)=x
\]

ultraweakly. Hence every fixed point lies in the weak closure of `pi_beta(D)`, while the reverse inclusion is obvious. Thus

\[
\boxed{
M_\beta^{\widetilde\phi_\beta}
=M_\beta^{\sigma}
=M_\beta^G
=\pi_\beta(\mathcal D)''.
}
\]

Since `D` is abelian, the modular centralizer of the canonical high-temperature KMS state is abelian. This statement is more precise than the coarse type-`III_1` classification in `PL-213`: the ambient factor is maximally non-semisfinite in Connes type, while the fixed algebra of this particular equilibrium modular flow is the weak cyclotomic diagonal.

## 3. Pedersen--Takesaki collapses every commuting same-sector state to a diagonal density

Gert K. Pedersen and Masamichi Takesaki proved the relevant noncommutative Radon--Nikodym theorem in “The Radon--Nikodym theorem for von Neumann algebras,” *Acta Mathematica* **130** (1973), 53--87, DOI `10.1007/BF02392262`.

For a faithful normal reference weight `phi` on a von Neumann algebra `M`, a normal semifinite weight `psi` invariant under the modular group of `phi` is represented by a unique positive self-adjoint operator `h` affiliated with the centralizer `M^phi`. In the state case this is the standard Pedersen--Takesaki notion that `psi` **commutes with** `phi`. Equivalently, the Connes cocycle derivative forms an ordinary one-parameter unitary group in the centralizer rather than a genuinely twisted cocycle.

Apply the theorem to `widetilde phi_beta`. The centralizer calculation above gives

\[
h\ \text{affiliated with}\ \pi_\beta(\mathcal D)''.
\]

Thus there is no hidden non-diagonal commuting perturbation inside the type-`III_1` factor. Every such relative density is measurable with respect to the same abelian diagonal that already survived the bounded scalar expectation in `PL-219`.

For the bounded faithful subfamily the formula is elementary and completely explicit. Let

\[
0<cI\le h\le CI,
\qquad h\in M_\beta^{\widetilde\phi_\beta}.
\]

Define

\[
\psi_h(x)
=
\frac{\widetilde\phi_\beta(h^{1/2}xh^{1/2})}
{\widetilde\phi_\beta(h)}.
\]

Since `h` lies in the centralizer, this is the normalized Pedersen--Takesaki perturbation. Its Connes cocycle derivative is

\[
[D\psi_h:D\widetilde\phi_\beta]_t
=
\left(\frac{h}{\widetilde\phi_\beta(h)}\right)^{it}.
\]

The logarithmic generator is therefore

\[
K_h
=
\log h-\log\widetilde\phi_\beta(h).
\]

The normalization subtracts only a scalar. All nontrivial spectral gaps of `K_h` are exactly those chosen in `log h`.

This classification closes more than the product-measure deformation considered in `PL-216`. There, the admissible densities were constructed by changing the independent prime-coordinate laws inside the same measure class. Here **every** normal state commuting with the canonical KMS state is controlled, including diagonal densities with arbitrary correlations among finitely or infinitely many prime coordinates, provided the corresponding affiliated operator defines a normal state/weight.

## 4. A one-prime clopen projection gives an exact programmability control

The diagonal spectrum is

\[
\widehat{\mathbb Z}
\cong\prod_p\mathbb Z_p.
\]

For a fixed prime `p`, the subset

\[
C_p
=
p\mathbb Z_p\times\prod_{q\ne p}\mathbb Z_q
\]

is clopen. Hence

\[
e_p=1_{C_p}\in C(\widehat{\mathbb Z})=\mathcal D
\]

is an actual `C*`-projection, not merely a measurable projection appearing only after weak closure.

By the canonical diagonal product law from `PL-215`,

\[
\Pr_{\mu_\beta}(v_p=k)
=(1-p^{-\beta})p^{-k\beta},
\qquad k\ge0.
\]

Therefore

\[
\widetilde\phi_\beta(e_p)
=
\Pr(v_p\ge1)
=p^{-\beta}.
\]

Choose any `a,b>0` and put

\[
h_{a,b}=a e_p+b(1-e_p).
\]

This is positive, bounded, invertible and belongs to the centralizer for every `beta>0`. Its normalizing scalar is

\[
c_{a,b}(\beta)
=
a p^{-\beta}+b(1-p^{-\beta}),
\]

so the relative modular generator is

\[
K_{a,b}
=
\left(\log a-\log c_{a,b}(\beta)\right)e_p
+
\left(\log b-\log c_{a,b}(\beta)\right)(1-e_p).
\]

Its two-point spectral gap is exactly

\[
\boxed{
\Delta K_{a,b}=\log(a/b).
}
\]

The temperature and the prime only affect the common scalar shift through `c_{a,b}(beta)`; they do not constrain the gap. As `a/b` ranges over `R_+`, the gap ranges over all of `R`.

This is a particularly strong matched control because no infinite-prime flexibility is needed. A **single prime coordinate** already supports arbitrary relative-modular spectral spacing. Passing to finite clopen partitions of `Zhat` permits arbitrary finite diagonal level structures, again subject only to the scalar state normalization.

Therefore a proposed coincidence between a finite set of relative-modular eigenvalue gaps and a finite set of zeta-zero ordinates is programmable rather than explanatory unless an independent arithmetic principle fixes `h`. Merely requiring `h` to be positive, normal, same-sector, centralizer affiliated, or built from canonical clopen prime events supplies no such principle.

## 5. The Riemann half is not selected

The conclusion holds uniformly throughout

\[
0<\beta\le1.
\]

Nothing in the centralizer identity changes at `beta=1/2`. The algebra

\[
M_\beta^{\widetilde\phi_\beta}
=
\pi_\beta(\mathcal D)''
\]

has the same structural origin at every high temperature, while the two-level control above works at every such `beta`. The probability `p^{-beta}` changes smoothly, but the freely chosen spectral gap `log(a/b)` is independent of it.

This keeps the distinct thresholds already separated by the preceding findings:

- `beta=1` is the Gibbs/symmetry-breaking and diagonal measure-class boundary (`PL-024`, `PL-215`);
- the whole interval `0<beta<=1` has type `III_1` (`PL-213`);
- the canonical temperature tangent has infinite diagonal Fisher length throughout that interval (`PL-216`);
- the square-free/Mobius observable has an `L^2` support threshold at `beta=1/2` but not a zero-sensitive phase transition (`PL-211`);
- bounded scalar and bounded correlation readouts reduce respectively to diagonal expectation and prime-gauge Fourier weights (`PL-219`, `PL-220`);
- commuting same-sector relative modular data now also reduces exactly to a diagonal density.

There is still no legitimate passage from any of these real-temperature statements to analytic continuation of `zeta(s)` in a complex variable. In particular the Pedersen--Takesaki density `h` is not an Euler product, and the cocycle parameter `t` is modular time rather than the imaginary part of a complex zeta argument.

## 6. Adversarial and novelty audit

Several overclaims must be excluded.

First, the result does **not** classify all faithful normal states on `M_beta`. Pedersen--Takesaki classifies the states commuting with the reference KMS state. A noncommuting state has a genuinely twisted Connes cocycle

\[
u_{s+t}=u_s\sigma_s^{\widetilde\phi_\beta}(u_t),
\]

and need not arise from a centralizer density. That noncommuting same-sector route remains open.

Second, the result does not say that every relative modular operator between arbitrary vectors is diagonal. The statement concerns Connes cocycles for the commuting Pedersen--Takesaki sector. Relative modular operators can live on the standard Hilbert space and carry additional left/right structure even when the cocycle is simple.

Third, the centralizer identity uses the **specific prime-gauge completion of the rational Bost--Connes system** proved in `PL-219`. It is not a generic theorem that a type-`III_1` factor has abelian centralizer. The proof works because the physical flow is dense in a compact gauge torus whose `C*` fixed-point algebra is exactly `D`.

Fourth, abelianness does not by itself imply irrelevance. A future construction could pick a particular diagonal `h` from a source-forced arithmetic rule and derive a nontrivial positivity or trace identity. The matched control says that the spectral data of an **unspecified** centralizer perturbation has no evidentiary force: arbitrary alternatives already satisfy all operator-algebraic admissibility conditions used here.

Fifth, the one-prime projection is not claimed to imitate global zeta arithmetic. It is deliberately a control showing that centralizer-relative spectral gaps are not rigid. Any positive proposal must identify a property that the rational-prime source forces and this one-prime programmable family cannot reproduce.

The novelty audit found no basis for a new theorem claim. Pedersen--Takesaki's 1973 theorem is exactly the classical classification needed once the centralizer has been identified, and standard KMS modular theory identifies physical and modular fixed points. Neshveyev's type-`III_1` theorem remains the ambient Bost--Connes factor source (`PL-213`). The new durable value for this research line is the **negative composition** of those classical facts with the compact prime-gauge result `PL-219` and the explicit prime-coordinate control from `PL-215`.

Primary literature anchors:

- Gert K. Pedersen, Masamichi Takesaki, “The Radon--Nikodym theorem for von Neumann algebras,” *Acta Mathematica* **130** (1973), 53--87. DOI `10.1007/BF02392262`.
- Masamichi Takesaki, *Tomita's Theory of Modular Hilbert Algebras and its Applications*, Lecture Notes in Mathematics **128**, Springer, 1970.
- Huzihiro Araki, “On the Kubo--Martin--Schwinger Boundary Condition,” *Progress of Theoretical Physics Supplement* **64** (1978), 12--20. DOI `10.1143/PTPS.64.12`.
- Sergey Neshveyev, “von Neumann Algebras Arising from Bost--Connes Type Systems,” *International Mathematics Research Notices* **2011**(1), 217--236. DOI `10.1093/imrn/rnq067`, arXiv `0907.1456`.
- Jean-Benoit Bost, Alain Connes, “Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory,” *Selecta Mathematica, New Series* **1** (1995), 411--457. DOI `10.1007/BF01589495`.

## Research consequence

The Bost--Connes branch now has a sharper exclusion ladder. Cross-temperature relative modular comparison is not a canonical same-factor operation (`PL-215`); the canonical temperature derivative is not an `L^2` same-sector tangent below `beta=1` (`PL-216`); and **every same-sector perturbation that does commute with the KMS state is forced back into the abelian cyclotomic diagonal and is spectrally programmable**.

Accordingly, a further modular pass should not search for an RH mechanism in an arbitrary density `h`, in its logarithm, or in the spectrum of a commuting Connes cocycle. The surviving question is narrower and falsifiable: can a genuinely noncommuting same-sector arithmetic state/weight or a canonical global trace/positivity construction impose a source-forced relation among prime channels that is absent from arbitrary type-`III_1` systems and cannot be reproduced by the diagonal programmable controls above?