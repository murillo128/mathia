# PF-181 — the area-preserving full-cusp handoff has summable weighted cost

**Status:** `LITERATURE+DERIVED + EXACT-AREA + POSITIVE/BOUNDARY`. PF-179 and PF-180 give an exact-area prime/shift comparison on the Lambert bodies and make the two halves of each one-cusp pant agree through the canonical cusp entry, but PF-180 deliberately stops before replacing that lower-pant map by one common deep-cusp normalization. In the standard cusp this remaining volume constraint is not an obstruction. The PF-179 outer branches are exact hyperbolic isometries, the physical left/right mismatch is the same adjacent first-difference mode already shown summable in PF-140, and PF-180's split correction has a fixed-scale summable taper at the cusp entry. Because the lower map preserves area exactly and both source and target one-cusp pants have the same Gauss--Bonnet area, its actual cusp trace satisfies an **exact zero-flux condition** in the flat cusp area coordinate. A fixed-slab relative Moser/Dacorogna correction can therefore keep the complete lower area-preserving germ, become the exact identity deeper in the cusp, and retain a summable inverse-unit-ball weighted metric budget. Thus the **full-cusp handoff is no longer part of the quantitative `rho=1` obstruction**. The remaining PF-175 gate is the compatible quantitative cuff/true-short-collar assembly and the final global two-sided weighted budget. No Schatten, scattering, determinant, resonance, or RH conclusion is claimed.

## Claim

For the `n`th exact prime/shift one-cusp pant write

\[
a_n=\frac{\ell_n}{2},\qquad a_n^+=a_n+\delta_n,
\]

and put

\[
\epsilon_n:=\log\frac{\cosh a_n^+}{\cosh a_n},
\qquad
d_n:=|\epsilon_n-\epsilon_{n+1}|.
\tag{1}
\]

PF-119/PF-122 give

\[
\boxed{\sum_n d_n<\infty.}
\tag{2}
\]

Let `F_n^{body}` be the area-preserving PF-179 Lambert maps after the PF-180 Hamiltonian split synchronization, chosen with the PF-180 taper equal to one on a fixed small Busemann neighborhood of the canonical cusp entry before it begins to turn off. This harmless fixed-cutoff choice leaves all PF-180 estimates unchanged and makes the two halves define one smooth area-preserving germ across the physical cusp entry.

After the same fixed-width smoothing of the split point used in PF-140, there is a nonnegative sequence `eta_n^{vol}` with

\[
\boxed{\sum_n\eta_n^{\mathrm{vol}}<\infty}
\tag{3}
\]

such that, in one fixed standard-cusp neighborhood of `y=1`, the common physical germ differs from the canonical normalized cusp gauge by `O(eta_n^{vol})` in a fixed `C^{1,\alpha}` hyperbolic norm. One admissible budget is

\[
\boxed{
\eta_n^{\mathrm{vol}}
:=
 d_n
 +\delta_n e^{-2a_n}
 +\delta_{n+1}e^{-2a_{n+1}}
 +|c_n|,
}
\tag{4}
\]

where `c_n` is the PF-134/PF-180 centered adjacent Lambert mode. PF-134, PF-114, and PF-107 imply (3).

There is a fixed `L>0` and, after a finite head, smooth diffeomorphisms from the source standard cusp to the target cusp-side complement of the lower body image,

\[
\boxed{
H_n:C_n\longrightarrow C_n^+,
}
\tag{5}

with all of the following properties:

1. `H_n` agrees with `F_n^{body}` on a whole neighborhood of the lower cusp interface;
2. `H_n` is exactly the identity in the common normalized cusp coordinates for all Busemann heights `r>=L`;
3. `H_n` preserves hyperbolic area exactly,
   \[
   \boxed{H_n^*d\mu_+=d\mu;}
   \tag{6}
   \]
4. `Bilip(H_n)<=1+C eta_n^{vol}` on the fixed handoff slab;
5. for every fixed exponent `s>=1`, with `W_g(z)=\mu_g(B_g(z,1))^{-1}` and the analogous target weight,
   \[
   \boxed{
   \int_{\mathrm{handoff}_n}W_g\,\delta_{g,H_n^*g_+}^{\,s}\,d\mu_g
   +
   \int_{H_n(\mathrm{handoff}_n)}W_{g_+}\,\delta_{g_+,(H_n^{-1})^*g}^{\,s}\,d\mu_{g_+}
   \le C_s(\eta_n^{\mathrm{vol}})^s.
   }
   \tag{7}
   \]

Consequently

\[
\boxed{
\sum_n\left[
\int W_g\,\delta^s d\mu_g
+
\int W_{g_+}\,\delta^s d\mu_{g_+}
\right]_{\mathrm{full\ cusp\ handoff}\ n}
<\infty
\qquad(s\ge1).
}
\tag{8}

Thus the area-preserving body/split stage can be handed to the exact deep-cusp identity at a cost strong enough for every PF-175 exponent `s>1` (indeed also at the `s=1` metric-weight level). The result is local to the cusp handoff and does not provide the remaining cuff/collar assembly or the complete-surface weighted estimate.

## 1. The PF-179/PF-180 cusp germ has an `ell^1` defect from the standard gauge

PF-140 already performs the physical cusp-chart calculation for the earlier PF-121/PF-139 comparison. Its key point is that the large one-Lambert common mode is a hyperbolic dilation/isometry; restoring the physical left/right charts leaves only the adjacent mode

\[
|\epsilon_n-\epsilon_{n+1}|=d_n
\tag{9}
\]

plus the exponentially small anchored Lambert remainder and the centered split correction.

The area-preserving construction is no worse at the cusp. PF-179 is **exactly isometric** on its outer Lambert branch, and equation (38) there shows that the difference between its `sinh` and `cosh` trace parameters is only `O(\delta e^{-2a})`. Repeating the physical rescaling in PF-140 therefore gives the same admissible boundary budget

\[
d_n+\delta_ne^{-2a_n}+\delta_{n+1}e^{-2a_{n+1}}.
\tag{10}
\]

PF-180 then changes the map only near the artificial split. At the canonical cusp entry both Lambert halves are already past their corners, the available two-sided width has an absolute positive lower bound, and the PF-180 taper is performed over one fixed Busemann scale. Its equations (29)--(39) therefore add a `C^{1,\alpha}` cusp-germ defect bounded by the centered adjacent mode `|c_n|` together with the same exponentially small remainders. A fixed-width smoothing of the one split kink costs the size of its derivative jump rather than an inverse shrinking scale. This proves (4) and the claimed fixed-germ estimate.

The important point is that **individual** `delta_n=O(1/p_n)` need not be summable. They occur at the cusp only inside exact isometries/common modes. The non-isometric physical handoff sees their adjacent difference or exponentially localized remainder, both already summable in persisted prime-flute evidence.

## 2. Exact area preservation forces zero cusp flux

Write the normalized standard cusp as

\[
C=\{(x,y):0\le x\le1,\ y\ge1\},
\qquad
g=\frac{dx^2+dy^2}{y^2}.
\tag{11}
\]

With `r=log y`,

\[
g=dr^2+e^{-2r}dx^2,
\qquad
d\mu=e^{-r}dx\,dr.
\tag{12}
\]

Introduce the exact area coordinate

\[
\boxed{z:=1-e^{-r}.}
\tag{13}
\]

Then

\[
\boxed{d\mu=dx\,dz,}
\qquad 0\le z<1
\tag{14}
\]

on the source standard cusp.

Let `K_n` be the source part of the pant below the canonical horocycle `y=1`. A one-cusp hyperbolic pant has area `2pi`, while the normalized cusp (11) has area `1`, so

\[
\operatorname{Area}(K_n)=2\pi-1.
\tag{15}
\]

The PF-179/PF-180 lower map is area preserving, hence its target image `K_n^+` also has area `2pi-1`. The complete target pant has area `2pi`, so its cusp-side complement has area **exactly one**.

Write the actual target boundary trace in the `(x,r)` chart as

\[
\Gamma_n(x)=(U_n(x),V_n(x)).
\tag{16}
\]

After the tail smallness in Section 1, `U_n` is an orientation-preserving circle diffeomorphism. In the area chart reparametrize the same geometric curve by `X=U_n(x)` and write

\[
H_n^{bd}(X)
:=1-e^{-V_n(U_n^{-1}(X))}.
\tag{17}
\]

The target region on the deep-cusp side of this graph has area

\[
\int_0^1\bigl(1-H_n^{bd}(X)\bigr)dX.
\tag{18}
\]

It must equal one by the preceding Gauss--Bonnet/area-preservation argument. Therefore

\[
\boxed{
\int_0^1 H_n^{bd}(X)dX=0.
}
\tag{19}

Equation (19) is the exact flux condition that the non-area-preserving PF-140 handoff did not need. It is not an asymptotic cancellation and does not depend on prime-gap estimates: it follows from exact area preservation of the lower map and equal total pant areas.

## 3. A fixed-slab relative volume correction preserves the whole lower germ

Choose fixed numbers `0<sigma<L/3`. For all sufficiently large `n`, the trace and its lower germ lie in the fixed two-sided standard cusp neighborhood from Section 1. Let `S=[0,L]xS^1` denote the source handoff slab, interpreted in `(r,x)` coordinates, and let `S_n^+` be the target region between the actual lower boundary germ and the standard horocycle `r=L`.

Keep the **actual PF-179/PF-180 area-preserving germ** on `0<=r<=sigma` and the exact identity germ on `r>=L-sigma`. A fixed-cutoff collar extension between them gives a smooth preliminary diffeomorphism

\[
E_n:S\longrightarrow S_n^+
\tag{20}
\]

with

\[
\|E_n-\operatorname{id}\|_{C^{1,\alpha}_g}
\le C\eta_n^{\mathrm{vol}}.
\tag{21}
\]

It is already area preserving on neighborhoods of both boundary components. The two slabs have equal total area: the cusp-side complement has area one by Section 2 and the common deep region `r>=L` has area `e^{-L}`, so each handoff slab has area `1-e^{-L}`. Consequently

\[
E_n^*d\mu_+-d\mu
\tag{22}
\]

is supported in one fixed interior subslab and has integral zero.

Apply the support-controlled relative Moser/Dacorogna correction on this **fixed nondegenerating domain**. Equivalently, choose a fixed bounded right inverse for `d` on compactly supported mean-zero top forms in the interior slab and run the usual Moser flow. The correction `phi_n` is the identity on neighborhoods of both boundaries and satisfies

\[
\phi_n^*E_n^*d\mu_+=d\mu.
\tag{23}
\]

Because the domain, support distance, cutoff scales, and background cusp geometry are all fixed, the standard local estimate has a constant independent of `n`:

\[
\|D\phi_n-I\|_{C^0_g}
\le C\eta_n^{\mathrm{vol}}.
\tag{24}
\]

Set

\[
H_n:=E_n\circ\phi_n.
\tag{25}
\]

Equations (21)--(25) prove exact area preservation, agreement with the complete lower body germ, exact deep-cusp identity, and the bilipschitz estimate in the claim. This is exactly the regime in which PF-178's warning about degeneration-dependent Moser constants disappears: no support width, injectivity scale, or pant-body distance is tending to zero in the handoff domain.

## 4. Fixed cusp height turns the metric estimate into a summable weighted budget

On `0<=r<=L`, the standard cusp has bounded geometry at the scale relevant to the handoff. PF-140 already records a uniform lower bound

\[
\mu_g(B_g(z,1))\ge c_L>0
\tag{26}
\]

for centers in this fixed-height slab, and the slab has uniformly bounded area. Equations (21) and (24) imply

\[
\delta_{g,H_n^*g_+}\le C_L\eta_n^{\mathrm{vol}}.
\tag{27}
\]

The target estimate follows from the inverse map; the tail bilipschitz constants tend to one, so the two unit-ball weights are uniformly comparable. Thus for every `s>=1`,

\[
\int W\,\delta^s d\mu
\le C_s(\eta_n^{\mathrm{vol}})^s
\tag{28}
\]

on both sides. Summing and using (3) gives (8). A finite exceptional head may be connected by arbitrary smooth area-preserving marked handoffs with finite total cost.

No infinite cusp depth is charged because `H_n` is exactly the normalized identity above the fixed height `L`.

## 5. What this closes and what remains open

PF-179 and PF-180 left four external/global requirements. PF-181 removes the cusp one at the exact strength needed by the `rho=1` route:

\[
\boxed{
\text{area-preserving body/split map}
+\text{exact zero cusp flux}
+\text{fixed-slab relative Moser}
\Longrightarrow
\text{area-preserving deep-cusp identity with summable weighted cost}.
}
\tag{29}
\]

The remaining geometric burden is now concentrated in the **closed interfaces**:

- choose quantitatively compatible area-preserving zero-twist germs at the distinguished decomposition cuffs;
- splice the complete body/cuff construction to every PF-177 optimized true short-collar gauge from the PF-138 family;
- prove the final source- and target-weighted `delta^s` budget after those overlapping collar/body interfaces are assembled in one smooth complete marking.

PF-181 does not imply that this final assembly exists. In particular it does not upgrade PF-177's local collar estimate to a compatible global map and it does not invoke PF-175 by itself.

## 6. Prior art and novelty audit

No novelty is claimed for Moser's volume-form argument, relative/support-controlled volume correction, hyperbolic cusp coordinates, or fixed-domain diffeomorphism extension.

The relevant classical/support-controlled sources were already audited in PF-178. In particular, Pedro Teixeira, *Dacorogna-Moser theorem on the Jacobian determinant equation with control of support*, Discrete and Continuous Dynamical Systems 37 (2017), 4071--4089, DOI `10.3934/dcds.2017173`, proves support control with optimal regularity for the prescribed-Jacobian problem; his addendum arXiv:1705.01416 treats the pullback equation between two prescribed equal-volume forms with the same support-control principle. Martins Bruveris, Peter W. Michor, Adam Parusiński, and Armin Rainer, *Moser's theorem on manifolds with corners*, Proceedings of the AMS 146 (2018), 4889--4897, DOI `10.1090/proc/14130`, records the boundary/corner extension of the classical Moser framework and traces the boundary case to Banyaga.

A fresh directed audit for area-preserving cusp boundary extension, support-controlled Moser on boundary/corner domains, and hyperbolic cusp handoffs recovered these general volume/symplectic tools but no theorem supplying the project-specific combination of the **PF-179/PF-180 exact-area lower germ**, PF-140's adjacent prime/shift cusp cancellation, and the exact zero-flux identity (19). Absence of such a source is not treated as a broad novelty theorem.

The durable custom content is the exact compatibility chain (29) and, especially, the observation that area preservation upgrades the cusp trace from merely small to **exactly flux-balanced**, allowing the quantitative correction to stay inside a fixed nondegenerating slab.

## 7. Audit / falsification core

A later adversary can test PF-181 through the following finite chain:

1. verify from PF-179 that the cusp-entry Lambert branches are exact isometries and that the only `sinh/cosh` parameter mismatch is `O(\delta e^{-2a})`;
2. repeat PF-140's physical left/right rescaling and verify that the non-isometric cusp-germ defect is bounded by (4), not by the nonsummable common `delta_n` mode;
3. inspect PF-180's fixed-width taper at `T_n^{cusp}` and verify that choosing it constant on a slightly larger initial cusp neighborhood preserves its estimates and gives one common area-preserving lower germ;
4. use Gauss--Bonnet plus exact lower-map area preservation to prove that the target cusp-side complement has area one;
5. change to `z=1-e^{-r}` and derive the exact mean-zero/flux identity (19);
6. construct the fixed-slab preliminary extension with the lower area-preserving germ and upper identity germ, verify equal slab areas and compact support of the density defect;
7. run the relative Moser correction on the fixed slab and check that its constants are independent of `n` because no geometric support scale degenerates;
8. use PF-140's fixed-height unit-ball lower bound to obtain (7)--(8) on both source and target sides;
9. preserve the evidence boundary: do **not** infer the global PF-175 weighted hypothesis, density-unitary Schatten membership, wave/scattering equivalence, determinants, resonances, or RH until the remaining closed-interface assembly is proved.

A refutation would have to break the `ell^1` cusp-germ estimate, the exact area/flux identity, the fixed-domain support correction, or the weighted estimate. Failure of the still-open cuff/true-short-collar assembly would not refute PF-181; it is precisely the remaining boundary recorded here.