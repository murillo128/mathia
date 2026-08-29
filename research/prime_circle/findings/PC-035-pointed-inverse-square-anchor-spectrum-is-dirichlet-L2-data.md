# PC-035 — the separately pointed inverse-square anchor profile is classical Dirichlet-L(2) data

**Status:** `LITERATURE+DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-NEGATIVE` for the most direct pointed repair of PC-034: retain the common vertex as a separately marked degree of freedom, use its inverse-square chord couplings to the primitive shell, and spectralize that profile by multiplicative characters. This does not rule out noncommuting pointed operators, nonlinear joint use of anchor and shell data, cross-level couplings, or global uniformization/monodromy.

## 1. The pointed escape left open by PC-034

PC-034 proves that after grounding all old vertices, the centered inverse-square chord operator cannot distinguish an odd level `n` from `2n`: the primitive-shell blocks are conjugate up to a universal scalar shift. Its explicit boundary is that a **genuinely pointed** construction might escape by keeping the common vertex `1` as a distinguished degree of freedom instead of absorbing it into the grounded background.

At an odd prime `p`, let

\[
\zeta_p=e^{2\pi i/p},
\qquad
G_p=(\mathbb Z/p\mathbb Z)^\times.
\]

The canonical pointed data supplied by the inverse-square chord energy are the couplings from the common anchor to every primitive vertex:

\[
w_p^-(a)
:=\frac1{|1-\zeta_p^a|^2}
=\frac1{4\sin^2(\pi a/p)},
\qquad a\in G_p.
\]

Unlike the grounded operator of PC-034, this vector remembers the anchor asymmetrically. It is therefore the first natural test of whether the pointed escape restores genuinely new arithmetic information.

It restores information, but its complete multiplicative harmonic content is already classical Dirichlet `L(2)` data.

## 2. Exact multiplicative spectrum of the pointed anchor profile

For a Dirichlet character `chi mod p`, define the multiplicative coefficient

\[
C_p^-(\chi)
:=\sum_{a=1}^{p-1}
\overline{\chi(a)}\,w_p^-(a).
\]

Use the classical Mittag-Leffler expansion

\[
\pi^2\csc^2(\pi x)
=\sum_{m\in\mathbb Z}\frac1{(x+m)^2}.
\]

At `x=a/p`,

\[
w_p^-(a)
=\frac{p^2}{4\pi^2}
\sum_{m\in\mathbb Z}\frac1{(a+mp)^2}.
\]

The series is absolutely convergent. Summing over `a=1,...,p-1` and observing that every nonzero integer not divisible by `p` has a unique representation `a+mp` gives

\[
\begin{aligned}
C_p^-(\chi)
&=\frac{p^2}{4\pi^2}
\sum_{\substack{n\in\mathbb Z\\n\ne0}}
\frac{\overline{\chi(n)}}{n^2}\\
&=\boxed{
\frac{p^2}{4\pi^2}
\bigl(1+\overline{\chi(-1)}\bigr)
L(2,\overline\chi)
}.
\end{aligned}
\]

Therefore

\[
\boxed{
C_p^-(\chi)=0
\quad\text{if }\chi(-1)=-1,
}
\]

while for every even character

\[
\boxed{
C_p^-(\chi)
=\frac{p^2}{2\pi^2}L(2,\overline\chi).
}
\]

For the principal character this reduces to

\[
C_p^-(\chi_0)
=\frac{p^2}{2\pi^2}\zeta(2)(1-p^{-2})
=\boxed{\frac{p^2-1}{12}},
\]

exactly the universal full-polygon degree that appears in PC-032/PC-034.

Thus the complete multiplicative harmonic decomposition of the **separately marked inverse-square anchor coupling** is no more mysterious than the logarithmic profile in PC-025: the logarithm yields `L(1,chi)`, while the inverse-square chord profile yields `L(2,chi)`.

## 3. Equivalent generalized-Bernoulli form

For a nonprincipal character modulo the prime `p`, hence a primitive character, the same coefficient can be written in the algebraic special-value form

\[
\boxed{
C_p^-(\chi)
=-\tau(\overline\chi)L(-1,\chi).
}
\]

For odd `chi`, both sides vanish. For even `chi`, use the standard generalized Bernoulli identity

\[
L(-1,\chi)=-\frac{B_{2,\chi}}2,
\]

with

\[
B_{2,\chi}
=p\sum_{a=1}^{p-1}\chi(a)B_2(a/p),
\]

and the Fourier series of `B_2`. The Gauss-sum identity gives

\[
B_{2,\chi}
=\frac{p\,\tau(\chi)}{\pi^2}
L(2,\overline\chi),
\]

and `tau(chi)tau(bar chi)=p` for even primitive `chi`, recovering the formula above.

This makes the novelty boundary explicit: the apparent pointed spectral data can equally be described as classical positive critical values `L(2,bar chi)` or generalized Bernoulli values `L(-1,chi)` with Gauss normalization.

## 4. The prime-versus-2p pointed difference is only the doubling character

The stronger test is the exact degeneracy that motivated PC-034. For odd prime `p`,

\[
\mu_{2p}^*=-\mu_p^*.
\]

After identifying the primitive vertices by `zeta_p^a -> -zeta_p^a`, their couplings to the **same fixed anchor** `1` become

\[
w_p^+(a)
:=\frac1{|1+\zeta_p^a|^2}
=\frac1{4\cos^2(\pi a/p)}.
\]

Pointing therefore really does break the raw half-turn congruence. But the extra information has an exact elementary form. The trigonometric identity

\[
\csc^2 x+\sec^2 x=4\csc^2(2x)
\]

gives, on `G_p`,

\[
\boxed{
w_p^+(a)=4w_p^-(2a)-w_p^-(a).}
\]

Let

\[
C_p^+(\chi)
:=\sum_{a=1}^{p-1}\overline{\chi(a)}w_p^+(a).
\]

Changing variables `b=2a mod p` in the first term yields

\[
\boxed{
C_p^+(\chi)
=\bigl(4\chi(2)-1\bigr)C_p^-(\chi).
}
\]

Hence for every even character

\[
\boxed{
C_p^+(\chi)
=\bigl(4\chi(2)-1\bigr)
\frac{p^2}{2\pi^2}L(2,\overline\chi),
}
\]

and all odd modes still vanish. For the principal mode,

\[
C_p^+(\chi_0)
=3C_p^-(\chi_0)
=\boxed{\frac{p^2-1}{4}}.
\]

So keeping the anchor **does** distinguish the `p` and `2p` pointed profiles, but only through the finite multiplicative action of doubling: each character mode is multiplied by `4 chi(2)-1`. There is no new spectral family hiding in the broken half-turn symmetry.

## 5. Why this is a decisive negative for the natural pointed repair

PC-034 left open the possibility that the distinguished common vertex could repair the information loss of grounded spectral shape. The most intrinsic repair is not an arbitrary added observable: the inverse-square chord operator itself already supplies the anchor-to-shell coupling vector `w_p^-`.

Its complete multiplicative spectrum is now classified exactly:

\[
\boxed{
\text{pointed inverse-square anchor fan}
\longrightarrow
\{L(2,\chi)\}_{\chi\bmod p}
}
\]

up to explicit powers of `p`, parity, and Gauss normalization. Under the prime/composite control `p <-> 2p`, the only additional factor is the character value at the doubling element `2`.

Therefore the route

\[
\boxed{
\text{separately mark the common anchor}
\to
1/\text{chord}^2\text{ profile}
\to
\text{multiplicative character spectrum/determinant}
\to
\text{new RH mechanism}
}
\]

is closed. Any zeros or special-value structure obtained after this diagonalization belong to the pre-existing Dirichlet `L`-package, not to a new prime-circle spectral mechanism.

This is the inverse-square pointed analogue of PC-025, but it closes a distinct escape created later by PC-032--PC-034 rather than re-running the logarithmic-chord calculation.

## 6. Prior art and novelty audit

No theorem-level novelty is claimed for the identities used here.

- The `csc^2` root-of-unity kernel is already classical in the Calogero--Perelomov family used for PC-032.
- Multiplicative characters and Gauss sums are the same classical harmonic-analysis package already encountered in PC-025.
- Generalized Bernoulli numbers and the identity `L(1-m,chi)=-B_{m,chi}/m` are standard; Szmidt--Urbanowicz--Zagier state this explicitly in their 1995 treatment of generalized Bernoulli numbers.
- The displayed `L(2)` formula follows directly from the absolutely convergent Mittag-Leffler expansion of `csc^2`; the `p <-> 2p` multiplier follows from one trigonometric identity and the multiplicative change of variables `a -> 2a`.

Targeted searches for cosecant-squared character sums, trigonometric character sums at positive integer `L`-values, and generalized Bernoulli formulations show that this sits squarely inside classical Dirichlet-character/special-value theory. Failure to locate this exact prime-circle phrasing is not treated as evidence of novelty.

The project-specific contribution is the **scope obstruction**: the first genuinely pointed repair suggested by PC-034 does recover the anchor asymmetry, but that recovered information immediately classicalizes to `L(2,chi)` plus the local doubling character `chi(2)`.

## 7. Boundary of the no-go

This finding does **not** say that every pointed operator is tautological.

In particular it does not classify:

- a noncommuting joint operator that retains both the primitive-shell block `A_n` and the anchor coupling as separate matrix data before diagonalization;
- nonlinear operations mixing several pointed profiles before taking characters;
- squarefree multi-prime radicals where the primitive deletion pattern itself remains nontrivial;
- cross-level operators that couple different `n` before spectralization;
- global pointed uniformization, monodromy, Liouville, or Weil--Petersson data of the PC-017 branch.

The surviving operator frontier is therefore stricter than merely "keep the anchor": **the anchor must participate in a genuinely nonseparable/noncommuting construction, rather than being reduced to its standalone multiplicative harmonic profile.**

## 8. Exact audit tests

The claim can be falsified without numerical fitting:

1. verify the Mittag-Leffler expansion of `csc^2` and the factor `p^2/(4 pi^2)`;
2. pair positive and negative integers to obtain the parity factor `1+bar chi(-1)`;
3. check the principal mode against the classical sum `sum csc^2(pi a/p)=(p^2-1)/3`;
4. verify `w_p^+(a)=4w_p^-(2a)-w_p^-(a)` exactly;
5. change variables `b=2a` to obtain `C_p^+=(4chi(2)-1)C_p^-`;
6. for nonprincipal even characters, independently recover `-tau(bar chi)L(-1,chi)` from generalized Bernoulli numbers.

Any failure of the parity factor, the principal mode, or the exact doubling multiplier would invalidate the classification.
