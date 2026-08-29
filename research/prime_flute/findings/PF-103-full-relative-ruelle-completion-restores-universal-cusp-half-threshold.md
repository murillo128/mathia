# PF-103 — full relative Ruelle completion restores the universal cusp half-threshold

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE` for interpreting the `Re s=1/4` boundary of the selected PF-084/PF-102 block sector as the natural convergence boundary of a full marked relative Ruelle/Selberg object. This does **not** rule out a full relative object for `Re s>1/2`, a further renormalization, or meromorphic continuation.

## Claim

A full marked primitive-orbit completion of the exact/projective prime-flute relative Ruelle sector must include primitive closed geodesics that wind arbitrarily many times around one cusp before closing through a second cusp. Already one fixed pair of distinct cusps produces a family

\[
\gamma_k=P_bP_d^k,
\qquad k\ge 1,
\]

whose lengths grow only as

\[
L_k=2\log k+O(1).
\]

For the exact endpoint flute and its projective reference, the `O(1)` term depends on the width-normalized two-cusp coefficient

\[
C_{bd}=\sqrt{W_bW_d}\,|d-b|.
\]

At least one actual marked prime-cusp pair has a nontrivial exact/reference coefficient ratio. For such a pair, the corresponding relative primitive-orbit logarithms are asymptotic to a nonzero constant times `k^{-2s}`. Hence this single primitive family is absolutely summable only for

\[
\boxed{\operatorname{Re}s>\frac12.}
\]

Therefore the selected all-block quarter-plane boundary of PF-084 cannot survive as the initial absolute-convergence boundary of a **full** marked relative Ruelle/Selberg completion. Cuspidal winding restores the universal parabolic half-threshold already seen from the transfer-operator side in PF-015.

## 1. Exact two-parabolic trace identity

PF-018 gives the parabolic around a cusp at the marked boundary point `b` in the form

\[
P_b(A)=
\begin{pmatrix}
2bA-1&2b^2A\\
-2A&-2bA-1
\end{pmatrix},
\qquad
W_b=2A,
\]

with `tr P_b=-2` and `det P_b=1`. For a second cusp `d` with parameter `B`, write

\[
P_d(B)=-I+N_d,
\qquad N_d^2=0.
\]

Then

\[
P_d(B)^k=(-1)^k(I-kN_d),
\]

and direct multiplication gives

\[
\boxed{
\left|\operatorname{tr}\bigl(P_b(A)P_d(B)^k\bigr)\right|
=
\left|W_bW_d(b-d)^2k-2\right|.
}
\tag{1}
\]

The sign in `SL(2,R)` depends on `k`; the absolute trace and the induced element of `PSL(2,R)` do not.

Define the width-one normalized cross-cusp coefficient used in PF-086/PF-087/PF-100,

\[
\boxed{
C_{bd}:=\sqrt{W_bW_d}\,|d-b|.
}
\tag{2}
\]

Then (1) is simply

\[
|\operatorname{tr}\gamma_k|=|C_{bd}^2k-2|.
\]

For all sufficiently large `k`, `\gamma_k` is hyperbolic and its primitive-orbit length satisfies

\[
2\cosh\frac{L_k}{2}=|\operatorname{tr}\gamma_k|.
\]

Therefore

\[
\boxed{
L_k=2\log k+2\log C_{bd}^2+o(1)
=2\log k+4\log C_{bd}+o(1).
}
\tag{3}
\]

This is an exact consequence of the orthogonal-circle/zero-twist Fuchsian generators. No prime-statistics approximation enters the trace identity.

## 2. The cusp-winding classes are distinct and primitive

Take a finite punctured-sphere subsurface containing the two cusps and an outer boundary. Its fundamental group is free, and the two peripheral cusp loops may be included among independent generators; the outer boundary absorbs the usual product relation of a closed punctured sphere.

The word represented by `\gamma_k=P_bP_d^k` has abelianization vector

\[
(1,k)
\]

in the two cusp coordinates. If `\gamma_k=\eta^r` with `r>1`, its abelianization would be divisible by `r`, impossible because

\[
\gcd(1,k)=1.
\]

Thus every sufficiently large hyperbolic `\gamma_k` is not a proper power, hence represents a primitive closed geodesic in the Selberg/Ruelle sense. Different `k` have different abelianizations, so the corresponding conjugacy classes are distinct.

The argument only needs the marked topological surface and is unchanged by the interior/exterior realization: ambient inversion conjugates/relabels the same peripheral classes and preserves absolute traces and lengths.

## 3. Exact/projective relative asymptotic

Apply the same marked word to the exact endpoint flute

\[
x_n^E=V(p_n)=\pi\cot\frac{\pi}{p_n}
\]

and to the projective reference

\[
x_n^0=p_n.
\]

For one fixed pair of cusps, set

\[
a_E=(C_{bd}^E)^2,
\qquad
a_0=(C_{bd}^0)^2,
\qquad
\rho=\frac{a_E}{a_0}
=\left(\frac{C_{bd}^E}{C_{bd}^0}\right)^2.
\]

The load-bearing fact that `\rho\ne1` for at least one **actual** marked prime-cusp pair follows exactly, without any recurrence assumption on fixed prime-gap patterns. For either realization write

\[
C_{ij}=\sqrt{W_iW_j}\,|x_j-x_i|.
\]

Suppose for contradiction that every marked pair agreed between the exact and projective flutes,

\[
C_{ij}^E=C_{ij}^0
\qquad(i\ne j).
\]

For four distinct ordered indices `i<j<k<l`, the cusp-width factors cancel from

\[
\frac{C_{ik}C_{jl}}{C_{ij}C_{kl}}
=
\frac{|x_k-x_i|\,|x_l-x_j|}
     {|x_j-x_i|\,|x_l-x_k|}.
\]

Hence equality of all `C_{ij}` would imply equality of all cross-ratios of the two marked endpoint sets

\[
\{p_n\}
\qquad\text{and}\qquad
\{V(p_n)\}.
\]

Fix three prime endpoints. There is a unique real Möbius transformation `M` sending those three projective endpoints to their exact images. Cross-ratio equality with the fixed triple is injective in the fourth point, so the assumed equality forces

\[
M(p_n)=V(p_n)
\qquad\text{for every prime }p_n.
\]

This is impossible. Write

\[
M(x)=\frac{ax+b}{cx+d}.
\]

Since the primes are unbounded and

\[
V(p)=p-\frac{\pi^2}{3p}+O(p^{-3}),
\]

we have `V(p_n)\to\infty`, so necessarily `c=0`. Thus `M(x)=\alpha x+\beta`. The same asymptotic gives

\[
\frac{V(p_n)}{p_n}\to1,
\qquad
V(p_n)-p_n\to0,
\]

hence `\alpha=1` and `\beta=0`. Therefore `M` would be the identity. But for every prime `p>2`, putting `y=\pi/p\in(0,\pi/2)` and using `\tan y>y` gives

\[
V(p)=\pi\cot\frac{\pi}{p}<p,
\]

contradicting `M(p)=V(p)`. Therefore

\[
\boxed{\exists\,i\ne j:\ C_{ij}^E\ne C_{ij}^0.}
\]

Choose such an actual marked prime-cusp pair for `b,d`; then `\rho\ne1`. PF-100 remains useful as a local finite-scale asymptotic description of the same coefficient defect, but it is not needed for this existence premise.

From (3),

\[
\boxed{
L_k^E-L_k^0
\longrightarrow
2\log\rho
=4\log\frac{C_{bd}^E}{C_{bd}^0}.
}
\tag{4}
\]

Consider the marked relative Ruelle factor for this primitive class,

\[
R_k(s)
=
\frac{1-e^{-sL_k^E}}
     {1-e^{-sL_k^0}}.
\]

For fixed `s` with `\sigma=\operatorname{Re}s>0`, (3)--(4) give

\[
e^{-sL_k^0}
=a_0^{-2s}k^{-2s}(1+o(1)),
\]

\[
e^{-sL_k^E}
=\rho^{-2s}a_0^{-2s}k^{-2s}(1+o(1)).
\]

Using `\log(1-z)=-z+O(z^2)`,

\[
\boxed{
\log R_k(s)
=
\bigl(1-\rho^{-2s}\bigr)
a_0^{-2s}k^{-2s}(1+o(1)).
}
\tag{5}
\]

If `\rho\ne1` and `\sigma>0`, the leading coefficient cannot vanish: `\rho^{-2s}=1` would force `\rho^{-2\sigma}=1`, hence `\rho=1`. Therefore

\[
\boxed{
\sum_{k\ge k_0}|\log R_k(s)|<\infty
\quad\Longleftrightarrow\quad
\operatorname{Re}s>\frac12.
}
\tag{6}
\]

For a Selberg-type product the `r=0` factor already contains this same obstruction, so adding the usual `r\ge1` factors cannot improve the absolute-convergence boundary.

Equation (6) is only a **necessary condition for a full product**. Other primitive families can make the global abscissa worse; nothing here proves convergence of the full infinite-type product for `Re s>1/2`.

## 4. Why this closes the PF-084 quarter-line branch

PF-084 selected the canonical simple block separators and obtained a sharp relative Ruelle-sector abscissa

\[
\operatorname{Re}s=\frac14.
\]

PF-102 then showed that the same quarter threshold can already be generated by one compact endpoint defect propagating through the one-dimensional family of long block geodesics.

One possible escape remained: perhaps that selected sector could be promoted to a natural **full marked primitive-orbit relative Ruelle product**, preserving `1/4` as its intrinsic convergence boundary. Equations (1)--(6) rule this out. Any faithful full primitive product must also contain the cusp-winding family `P_bP_d^k`, and that subfamily alone has the universal `k^{-2s}` barrier

\[
\boxed{
\operatorname{Re}s=\frac12.
}
\]

Thus the quarter-plane boundary is a property of the selected non-winding block family, not the natural initial boundary of a full primitive-orbit completion.

This is the orbit-side counterpart of PF-015. There the accelerated parabolic transfer block contains the standard sum

\[
\sum_{k\ge1}(kw+z)^{-2s}
\]

and therefore begins at `Re s>1/2`. PF-103 shows that passing to **relative exact/projective closed-orbit data does not cancel this universal cusp mechanism**: winding between two distinct cusps leaves a nonzero relative coefficient and restores the same exponent.

## 5. Universal control: no primes or cotangent tail are needed

The phenomenon is not prime-specific. In the regular reference lattice `x_n=n`, the cusp parabolics satisfy

\[
|\operatorname{tr}(P_mP_n^k)|
=16(n-m)^2k+O(1).
\]

Move only one endpoint, `x_m\mapsto m+\delta`, with `0<|\delta|<1/2`, leaving the entire tail unchanged. The corresponding trace slope changes by a nonunit constant (equivalently the normalized `C_{mn}` changes), so the relative winding factors again satisfy

\[
|\log R_k(s)|\asymp k^{-2\operatorname{Re}s}.
\]

Hence the `1/2` barrier persists for a single compact geometric defect. Its appearance in a full relative product therefore cannot be evidence for prime gaps, the exact cotangent tail, or the Riemann critical line.

## 6. Prior art / novelty audit

The ingredients are classical and no novelty is claimed for them separately.

- Cuspidal acceleration of transfer operators produces parabolic power sums with the universal initial condition `Re s>1/2`; this is explicit in the slow/fast transfer-operator literature, including Alexander Adam and Anke Pohl, *A transfer-operator-based relation between Laplace eigenfunctions and zeros of Selberg zeta functions*, ETDS 40 (2020), DOI `10.1017/etds.2018.51`.
- Fedosova--Pohl, *Meromorphic continuation of Selberg zeta functions with twists having non-expanding cusp monodromy*, Selecta Math. 26 (2020), DOI `10.1007/s00029-019-0534-3`, treats geometrically finite Fuchsian groups and explains the role of cuspidal acceleration/Hurwitz-Lerch continuation in a strict transfer-operator framework.
- Pohl--Wabnitz, *Selberg Zeta Functions, Cuspidal Accelerations, and Existence of Strict Transfer Operator Approaches*, Memoirs AMS 1616 (2026), DOI `10.1090/memo/1616`, gives a systematic cuspidal-acceleration/Fredholm construction for geometrically finite noncompact hyperbolic orbisurfaces.
- Cusp-winding statistics and thermodynamic formalisms for finitely generated Fuchsian groups are an established subject; recent examples include work of Yuya Arima and of Arima--Jaerisch. These settings are much more controlled than the infinitely generated prime-flute.

Directed searches did not locate the specific relative statement proved here: for the prime-flute's explicit zero-twist parabolics, the exact identity `|tr(P_bP_d^k)|=|C_{bd}^2k-2|` combines with the exact cross-ratio rigidity argument above to force a nontrivial exact/projective coefficient and hence a `1/2` subseries inside **any marked full primitive-orbit completion** of the PF-084 sector.

Accordingly, the novelty is a program-specific negative consequence, not a new theorem about standard cusped Selberg theory.

## 7. Scope and surviving possibilities

PF-103 does **not** establish a full Selberg/Ruelle zeta for the prime-flute. PF-035 still blocks the ordinary unrenormalized Euler product because primitive lengths accumulate at zero, and the standard geometrically finite transfer-operator theorems do not apply to this infinitely generated surface.

It also does not exclude a more radical renormalization that explicitly removes cusp-winding families, nor a meromorphic continuation of some independently constructed relative object. But any such subtraction would have to justify why removing the universal cusp sector is canonical and what prime-sensitive information survives; simply observing a boundary at `1/2` would add no RH evidence because PF-015 and the compact-defect control already make that exponent universal.

The stable conclusion is therefore

\[
\boxed{
\text{selected block }1/4
\;\not\longrightarrow\;
\text{full relative Ruelle }1/4,
}
\]

and, more specifically,

\[
\boxed{
\text{full marked primitive completion}
\;\Longrightarrow\;
\text{universal cusp-winding obstruction at }\operatorname{Re}s=\tfrac12.
}
\]

## 8. Formalizable core

The finite algebraic part is a good Lean candidate:

1. verify `det P_b(A)=1`, `tr P_b(A)=-2`, and `(P_d(B)+I)^2=0`;
2. prove
   \[
   |\operatorname{tr}(P_b(A)P_d(B)^k)|
   =|4AB(b-d)^2k-2|;
   \]
3. rewrite `4AB(b-d)^2=W_bW_d(b-d)^2=C_{bd}^2`;
4. prove that equality of all marked `C_{ij}` between the projective endpoints `p_n` and exact endpoints `V(p_n)` forces equality of all cross-ratios and hence a single Möbius map `M` with `M(p_n)=V(p_n)` for every prime;
5. use the cotangent asymptotic and `V(p)<p` for `p>2` to rule out such an `M`, establishing an actual pair with `\rho\ne1`;
6. derive `L_k=2 arcosh(|tr|/2)=2 log k+2 log C_{bd}^2+o(1)`;
7. prove the elementary `p`-series implication (5)--(6) under `\rho>0`, `\rho\ne1`, `Re s>0`.

The only topological input needed for primitivity is that the two peripheral loops are independent in the abelianization of a finite punctured-sphere subsurface with boundary.