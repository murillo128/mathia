# ANF-124 — coalescing-saddle pairs have a strict Gaussian coherence gap

**Status:** `EXACT-DERIVED + COALESCING-SADDLE-GRAM + LOCAL-GAUSSIAN-AFFINITY + PHASE-RESOLVED-KERNEL + STRICT-PAIR-COHERENCE-GAP + SINGLE-TRANSLATE-MIRROR-BARRIER`. `ANF-123` leaves one low-budget transverse chamber after separated saddles become exponentially expensive: different `ANF-115` packet families whose parameters differ by `Theta(A^(-1/2))`, so their saddles remain only `O(1)` apart in the Gaussian coordinate `u=sqrt(A)(alpha-a_0)`. That chamber has an explicit two-profile limit. The normalized Montgomery--Taylor source overlap converges to a Gaussian coherent-state kernel, and two genuinely different coalescing families remain separated by a strict Hilbert angle even after the optimal horizontal translation is chosen.

It is useful to expose the integer parameter already present in the exact `ANF-115` construction. For every positive integer `n` let `P_{A,n}` denote the packet obtained from

\[
t_{k,A}=\frac12+A^{-2}3^{-k},
\qquad
1\le k\le n,
\]

with the same heights `+-iA/(4pi)`. Thus `ANF-115` is the specialization `n=floor(gamma A)`. Fix `gamma_0>0`, put

\[
n_{0,A}=\lfloor\gamma_0A\rfloor,
\qquad
n_{r,A}=n_{0,A}+\lfloor\kappa_r\sqrt A\rfloor,
\qquad
P_{r,A}=P_{A,n_{r,A}},
\]

for fixed real `kappa_r`; all `n_{r,A}` are positive for large `A`. Write

\[
E_{r,A}=E_0(P_{r,A}),
\qquad
\delta\kappa=\kappa_r-\kappa_s,
\]

and retain the `ANF-115` saddle data

\[
a_\gamma=\frac2\pi\arctan\frac1{\pi\gamma},
\qquad
f(\gamma)=F_\gamma(a_\gamma),
\qquad
c_0=-F_{\gamma_0}''(a_{\gamma_0})
=\frac{1+\pi^2\gamma_0^2}{2\gamma_0}.
\tag{1}
\]

Then

\[
\boxed{
f''(\gamma_0)
=\frac{2}{\gamma_0(1+\pi^2\gamma_0^2)}
=\frac1{c_0\gamma_0^2}>0.}
\tag{2}
\]

The absolute source affinity of two coalescing families has the limit

\[
\boxed{
\frac{
\displaystyle\int_{-1}^{1}J_0(\alpha)
|S_{P_{r,A}}(\alpha)|
|S_{P_{s,A}}(\alpha)|\,d\alpha
}{\sqrt{E_{r,A}E_{s,A}}}
\longrightarrow
\exp\!\left[-\frac{f''(\gamma_0)}8(\delta\kappa)^2\right].
}
\tag{3}
\]

Hence arbitrary real translations cannot increase the normalized Montgomery--Taylor cross coherence beyond

\[
\boxed{
\limsup_{A\to\infty}
\frac{|\mathcal C_0(P_{r,A}+\tau_{r,A},P_{s,A}+\tau_{s,A})|}
{\sqrt{E_{r,A}E_{s,A}}}
\le
\rho(\delta\kappa)
:=
\exp\!\left[-\frac{(\delta\kappa)^2}
{4\gamma_0(1+\pi^2\gamma_0^2)}\right].
}
\tag{4}
\]

The ceiling is strict whenever `delta kappa != 0` and is sharp. More precisely, if

\[
\frac{\tau_{r,A}-\tau_{s,A}}{\sqrt A}\longrightarrow\delta s,
\]

the phase-resolved two-profile kernel has modulus

\[
\boxed{
K_0(\delta\kappa,\delta s)
=
\exp\!\left[
-\frac{f''(\gamma_0)}8(\delta\kappa)^2
-\frac{\pi^2}{2c_0}
\left(\frac{\delta\kappa}{2}+2\delta s\right)^2
\right].
}
\tag{5}
\]

An `O(1)` translation adjustment tunes the center phase without changing `delta s`, and choosing

\[
\boxed{\delta s=-\frac{\delta\kappa}{4}}
\tag{6}
\]

removes the second attenuation factor. Thus the best possible pairwise coherence is exactly the amplitude-affinity ceiling `rho(delta kappa)` in (4).

A direct consequence is a strict obstruction to mirroring the base packet with one translated coalescing family. Let `kappa != 0` be fixed, let

\[
n_{\kappa,A}=n_{0,A}+\lfloor\kappa\sqrt A\rfloor,
\qquad
P_{\kappa,A}=P_{A,n_{\kappa,A}},
\]

and allow arbitrary positive integer multiplicities `w_A` and arbitrary real translations `tau_A`. Then

\[
\boxed{
\liminf_{A\to\infty}
\frac{E_0\!\left(
P_{0,A}\sqcup w_A(P_{\kappa,A}+\tau_A)
\right)}{E_{0,A}}
\ge
1-\rho(\kappa)^2
=
1-
\exp\!\left[
-\frac{\kappa^2}
{2\gamma_0(1+\pi^2\gamma_0^2)}
\right]
>0.
}
\tag{7}
\]

So the first transverse chamber left by `ANF-123` does **not** contain a two-profile analogue of the exact same-saddle cancellation in `ANF-122`: a single distinct coalescing packet family, even optimally translated and with arbitrary multiplicity, cannot make the combined source norm vanish on the scale of the base packet. To obtain asymptotic full mirroring from this packet class one must approach the diagonal more finely than `A^(-1/2)` or use a genuinely multi-component span of coalescing profiles/translations.

## 1. The coalescing family is an exact critical-size translation cloud

The exact `ANF-115` subset-product structure has a useful nesting property which is hidden when the family is indexed only by `gamma`. If `n_1>=n_0`, then every subset of `{1,...,n_1}` splits uniquely into an old subset and a subset of the new indices. Therefore

\[
\boxed{
P_{A,n_1}
=
\bigsqcup_{T\subset\{n_0+1,\ldots,n_1\}}
\left(
P_{A,n_0}
+\sum_{k\in T}t_{k,A}
\right).
}
\tag{8}
\]

Thus a positive parameter shift is **exactly** a positive translation cloud of the smaller packet, with cloud size

\[
V_A=2^{n_1-n_0}.
\tag{9}
\]

At the coalescing scale `n_1-n_0=kappa sqrt(A)+O(1)`,

\[
\boxed{
\log V_A
=(\kappa\log2)\sqrt A+O(1).
}
\tag{10}
\]

This explains why the chamber is not already covered by `ANF-118`--`ANF-122`. Their uniform same-saddle comparison assumes `log(e+V_A)=o(A^(1/3))`, while the cloud required to shift the `ANF-115` saddle by one Gaussian width naturally has logarithmic weight `Theta(sqrt(A))`. The new regime is therefore the first scale at which exact packet nesting outruns the fixed-saddle cloud envelope while the two saddle peaks still overlap at order one.

The identity also gives a useful falsification check. When `delta kappa=0`, equation (3) gives affinity one, consistent with the fact that one is comparing the same packet family. A nonzero fixed `delta kappa` changes only `Theta(sqrt(A))` factors out of `Theta(A)`, yet that is already enough to produce a constant Hilbert angle after source normalization.

## 2. The amplitude overlap is a local Hellinger affinity

Write

\[
X_{n,A}=\sum_{k=1}^n t_{k,A}
=\frac n2+O(A^{-2}).
\tag{11}
\]

On every fixed neighborhood of the positive saddle, all cosine factors are positive for large `A`, and the exact subset product may be written

\[
Q_{A,n}(\alpha)
=
2^n
\exp[-\pi i\alpha X_{n,A}]
\prod_{k=1}^n\cos(\pi\alpha t_{k,A}).
\tag{12}
\]

Together with the common height factor,

\[
S_{P_{A,n}}(\alpha)
=2\cosh(A\alpha/2)Q_{A,n}(\alpha).
\tag{13}
\]

Take two indices `n_r,n_s` above and put

\[
\bar\gamma_A=\frac{n_{r,A}+n_{s,A}}{2A}.
\]

Multiplying the magnitudes in (13), the logarithm of the cross density on a fixed saddle neighborhood is

\[
A F_{\bar\gamma_A}(\alpha)+B_{rs,A}(\alpha),
\tag{14}
\]

where `B_{rs,A}` and its first two derivatives are uniformly bounded. This is the same bounded-prefactor mechanism used in `ANF-118`: the ternary perturbations have total size `O(A^(-2))`, the floor errors are bounded, and `J_0` is smooth and positive at the limiting interior saddle. Strict concavity gives the same Gaussian tails outside that neighborhood, uniformly for these `A^(-1/2)` parameter shifts.

Laplace expansion at `a_{bar gamma_A}` therefore yields

\[
\frac{
\displaystyle\int J_0|S_{P_{r,A}}||S_{P_{s,A}}|
}{\sqrt{E_{r,A}E_{s,A}}}
=
\exp\!\left[
A\left(
 f(\bar\gamma_A)
-\frac{f(\gamma_{r,A})+f(\gamma_{s,A})}{2}
\right)
\right](1+o(1)),
\tag{15}
\]

where `gamma_{r,A}=n_{r,A}/A`. The Gaussian normalization factors and bounded prefactors cancel to `1+o(1)` because all three parameters converge to `gamma_0`.

The envelope theorem applied to

\[
f(\gamma)=F_\gamma(a_\gamma)
\]

gives

\[
f'(\gamma)
=2\log\cos\frac{\pi a_\gamma}{2}
=\log\frac{\pi^2\gamma^2}{1+\pi^2\gamma^2},
\]

and differentiating once more gives (2). Since

\[
\gamma_{r,A}
=\gamma_0+\frac{\kappa_r}{\sqrt A}+O(A^{-1}),
\qquad
\gamma_{s,A}
=\gamma_0+\frac{\kappa_s}{\sqrt A}+O(A^{-1}),
\]

a second-order expansion gives

\[
\boxed{
A\left(
 f(\bar\gamma_A)
-\frac{f(\gamma_{r,A})+f(\gamma_{s,A})}{2}
\right)
\longrightarrow
-\frac{f''(\gamma_0)}8(\delta\kappa)^2.
}
\tag{16}
\]

Equations (15)--(16) prove (3). This is exactly the local square-root-density/Hellinger geometry of two nearby Gaussian saddles: in the coordinate `u=sqrt(A)(alpha-a_0)`, the two normalized magnitude profiles have the same limiting variance but centers separated by a fixed amount. The strict affinity loss is therefore an **amplitude** effect and cannot be repaired by any horizontal translation, which changes only phase.

## 3. The translation degree of freedom supplies the second Gaussian coordinate

The phase in (12) shows exactly what a horizontal translation can do. For translated packets, the positive-saddle cross integrand acquires

\[
\exp\!\left[
-\pi i\alpha
\left(
X_{n_r,A}-X_{n_s,A}
+2(\tau_{r,A}-\tau_{s,A})
\right)
\right].
\tag{17}
\]

Suppose

\[
\frac{\tau_{r,A}-\tau_{s,A}}{\sqrt A}\to\delta s.
\]

On the Laplace coordinate

\[
\alpha=a_{\bar\gamma_A}+\frac u{\sqrt A},
\]

equation (11) makes the coefficient of `u` converge to

\[
\boxed{
\beta
=\pi\left(\frac{\delta\kappa}{2}+2\delta s\right).
}
\tag{18}
\]

The limiting Gaussian integral contributes its characteristic function

\[
\exp\!\left[-\frac{\beta^2}{2c_0}\right].
\tag{19}
\]

The negative saddle is the complex conjugate of the positive one, so the full real Montgomery--Taylor cross term is the real part of twice the positive-saddle integral. Consequently there is an explicit center phase `Theta_A` such that

\[
\frac{\mathcal C_0(P_{r,A}+\tau_{r,A},P_{s,A}+\tau_{s,A})}
{\sqrt{E_{r,A}E_{s,A}}}
=
K_0(\delta\kappa,\delta s)\cos\Theta_A+o(1),
\tag{20}
\]

with `K_0` given by (5). Changing one translation by a bounded amount changes `Theta_A` by an order-one nondegenerate amount because `a_{gamma_0}>0`, while it changes `delta s` only by `o(1)`. Hence the cosine can be tuned asymptotically to either sign without changing the limiting modulus. Choosing (6) makes `beta=0` and proves the sharpness of (4).

There is also a translation-uniform proof of the ceiling which avoids any assumption on the scale of `tau_{r,A}-tau_{s,A}`. Cauchy--Schwarz after taking absolute values of the cross integrand gives

\[
|\mathcal C_0(P_{r,A}+\tau_{r,A},P_{s,A}+\tau_{s,A})|
\le
\int J_0|S_{P_{r,A}}||S_{P_{s,A}}|,
\tag{21}
\]

and (3) immediately yields (4) for arbitrary translations. Thus no very large translation can evade the amplitude mismatch.

## 4. A single coalescing family cannot realize full profile mirroring

Fix the base family `kappa=0` and one nonzero coalescing offset `kappa`. Let

\[
t_A
:=
w_A\sqrt{\frac{E_{\kappa,A}}{E_{0,A}}}
\ge0,
\]

and let

\[
r_A
:=
\frac{\mathcal C_0(P_{0,A},P_{\kappa,A}+\tau_A)}
{\sqrt{E_{0,A}E_{\kappa,A}}}.
\]

Expanding the source norm gives the exact scalar identity

\[
\frac{E_0\!\left(P_{0,A}\sqcup w_A(P_{\kappa,A}+\tau_A)\right)}{E_{0,A}}
=1+t_A^2+2t_Ar_A.
\tag{22}
\]

By (4), `|r_A|<=rho(kappa)+o(1)`. Therefore, uniformly in the multiplicity and translation,

\[
1+t_A^2+2t_Ar_A
\ge
1+t_A^2-2(\rho(\kappa)+o(1))t_A
\ge
1-(\rho(\kappa)+o(1))^2,
\tag{23}
\]

which proves (7).

This lower bound deliberately relaxes the physical integer multiplicity to an arbitrary nonnegative scalar amplitude before optimizing, so integrality cannot weaken it. It is also rate-sharp at the Hilbert-pair level: after the optimal `sqrt(A)` translation slope (6) and bounded phase tuning, the normalized cross coherence approaches `-rho(kappa)`. Whether an integer multiplicity can simultaneously hit the optimal scalar norm ratio is irrelevant to the obstruction; failure to do so only increases the residual.

The conclusion is narrower than `ANF-122` and complementary to it. `ANF-122` treats arbitrarily complicated positive translation clouds of the **same** packet inside its uniform cloud envelope and shows that a full saddle-band mirror becomes globally excisable. Here the packet family itself changes at the critical coalescing scale outside that envelope, and the result says that one translated copy of a genuinely different coalescing family cannot even produce full source mirroring in the first place.

## 5. Prior-art boundary, stress tests, and the remaining completion gate

The Gaussian structure in (3)--(5) is not novel in isolation. A targeted prior-art audit found two classical neighboring descriptions. In local asymptotic normality/Hellinger geometry, square-root densities under `1/sqrt(n)` parameter shifts acquire a Gaussian affinity governed to second order by Fisher information, with the familiar `1/8` coefficient. In the Bargmann--Fock/coherent-state language originating with Bargmann's 1961 analytic Hilbert-space transform, normalized Gaussian wave packets have overlaps that decay exponentially with squared phase-space separation. These are the correct generic analogues of (3)--(5).

No external theorem is load-bearing here. The Mathia-specific content is the direct derivation from the exact `ANF-115` product: the local parameter metric is the explicit curvature

\[
f''(\gamma_0)=\frac{2}{\gamma_0(1+\pi^2\gamma_0^2)},
\]

while horizontal translation couples to the second coordinate through the exact combination `delta kappa/2+2 delta s`. The resulting strict physical pair-mirror floor (7), and the identification (8)--(10) of the coalescing family with the first exact translation cloud beyond the `ANF-118` envelope, are specific to the persisted Montgomery--Taylor packet model. Because the proof rederives the needed Gaussian limit from that product, no new source anchor is required and `SOURCES.md` is unchanged.

The controls behave correctly. At `delta kappa=0`, the affinity ceiling is one. For fixed nonzero `delta kappa`, the optimal translation cancels only the phase-gradient mismatch and leaves the positive amplitude penalty in (3). Sending `|delta s|` away from the optimizer makes the phase-resolved coherence strictly smaller. The strict residual floor survives arbitrary multiplicity because it is simply the distance from one normalized Hilbert vector to the ray generated by another.

The finding does **not** close the bounded fatal branch of `ANF-119`--`ANF-121`. `ANF-121` shows that fatal triangular-notch exposure remains uniformly below pointwise efficiency saturation, so a fatal completion need not demand exact full mirroring. Nor does (7) rule out a companion built from several translated coalescing families: a multi-profile span can have much richer cancellation than one ray, and Gaussian coherent states are precisely a setting where such spans can be highly nontrivial.

The live packetized completion question is therefore sharpened to a finite-/growing-span problem for the coalescing kernel (5): determine whether a positive multiset combination of several `A^(-1/2)`-separated families and translations can satisfy the `ANF-119` polarization requirement while leaving enough central-notch exposure to reach the `ANF-099` fatal envelope. Any such construction must now exploit genuinely multi-component coherent-state geometry; a single wrong coalescing profile is quantitatively insufficient.