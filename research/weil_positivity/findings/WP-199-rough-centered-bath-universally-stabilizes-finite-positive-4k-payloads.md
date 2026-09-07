# WP-199 — A rough centered bath can stabilize every finite monotone-positive `4k` payload

**Status:** `DERIVED + EXACT + INFINITE-DIMENSIONAL + UNIVERSAL-FINITE-PAYLOAD-STABILIZATION + FULL-WEIL-AUTOCORRELATION-CONE + MONOTONE-POSITIVE + MATCHED-CONTROL + NONARITHMETIC + DECISIVE-NARROWING + PRIOR-ART-CLASSICALIZATION + NOT-A-WEIL-BRIDGE`.

`WP-197` proves a complete finite-dimensional obstruction: for every finite-dimensional pair `H>=0`, `V>=0`, full order-`4k` positivity on the real Weil autocorrelation cone forces `HV=0`. `WP-198` then shows that this rigidity fails in the natural infinite Schatten class `S^{4k}` by adjoining enough copies of one rough source-centered bath to one off-zero scalar channel.

The scalar payload in `WP-198` is not special. The same bath can absorb the entire Weil-cone sign defect of **any fixed finite-dimensional monotone-positive pair**, commuting or noncommuting. More precisely, let

\[
n=4k,
\tag{1}
\]

and let `(H_f,V_f)` be arbitrary finite-dimensional self-adjoint matrices with

\[
H_f\ge0,\qquad V_f\ge0.
\tag{2}
\]

Then there is an integer `M>=1` such that, after adjoining `M` orthogonal copies of the centered `WP-198` bath,

\[
\widetilde H
=
0_{\rm bath}^{\oplus M}\oplus H_f,
\qquad
\widetilde V
=
V_{\rm bath}^{\oplus M}\oplus V_f,
\tag{3}
\]

one has

\[
\widetilde H\ge0,
\qquad
\widetilde V\ge0,
\qquad
\widetilde V\in\mathcal S^n\setminus\mathcal S^{n-1},
\tag{4}
\]

and nevertheless

\[
\boxed{
\mathcal R_n(g*\widetilde g;\widetilde H,\widetilde V)>0
\qquad
\text{for every nonzero real }
g\in C_c^\infty(\mathbb R).
}
\tag{5}
\]

No algebraic restriction is imposed on the finite payload beyond positivity. In particular, `H_fV_f` may be nonzero and `[H_f,V_f]` may be nonzero. Thus the rough centered reservoir is a **universal finite-payload stabilizer** for this order mechanism.

This materially strengthens the matched control. Once arbitrary orthogonal rough reservoirs in `S^{4k}\setminus S^{4k-1}` are admitted, full Weil-cone positivity does not merely fail to force zero-mode support: it can be manufactured around any finite positive spectral geometry whatsoever. Therefore arithmetic information confined to a finite sector cannot become explanatory merely because an unrelated infinite bath makes the completed form positive. A viable Mathia completion has to derive and couple its critical reservoir intrinsically before the sign theorem, rather than appending a generic positive stabilizer after the arithmetic payload is chosen.

## 1. Every finite payload has only an `O(|xi|^{-1})` sign defect

Let `eta_f` be the order-`n` higher-order spectral-shift density of `(H_f,V_f)`, and write

\[
G_f(\xi)
=
\widehat{\eta_f^{\rm ev}}(\xi).
\tag{6}
\]

Finite-dimensional higher-order spectral-shift theory gives a compactly supported density that is piecewise absolutely continuous away from the finite source spectrum. `WP-197` records the distributional derivative in the form

\[
D\eta_f
=q+
\sum_{\lambda\in\sigma(H_f)}
J_\lambda\delta_\lambda,
\qquad q\in L^1(\mathbb R),
\tag{7}
\]

with, at `n=4k` and `V_f>=0`,

\[
J_\lambda
=
\frac1{(n-1)!}
\operatorname{Tr}
\left((P_\lambda V_fP_\lambda)^{n-1}\right)
\ge0.
\tag{8}
\]

Fourier transformation and Riemann--Lebesgue therefore give

\[
G_f(\xi)
=
-\frac1\xi
\sum_{\lambda\in\sigma(H_f)}
J_\lambda\sin(\lambda\xi)
+o(|\xi|^{-1}).
\tag{9}
\]

In particular there are constants `C_f,R_f>0` such that

\[
\boxed{
|G_f(\xi)|\le \frac{C_f}{|\xi|}
\qquad(|\xi|\ge R_f).
}
\tag{10}
\]

Also `G_f` is continuous on the whole real line because `eta_f in L^1`.

Equation (10) is all that the stabilization argument needs. The detailed finite spectrum, commutation relations, and source-jump phases can be arbitrary.

## 2. The `WP-198` bath has a slower strictly positive Fourier floor

Use exactly the centered bath from `WP-198`. On `ell^2(N)`,

\[
H_0=0,
\qquad
V_0=\operatorname{diag}(a_1,a_2,\ldots),
\qquad
 a_j=j^{-2/(2n-1)}.
\tag{11}
\]

Then

\[
V_0\in\mathcal S^n\setminus\mathcal S^{n-1}.
\tag{12}
\]

Let

\[
F_0(\xi)
=
\widehat{\eta_{n,0,V_0}^{\rm ev}}(\xi).
\tag{13}
\]

`WP-198` proves two decisive properties:

\[
F_0(\xi)>0
\qquad(\xi\in\mathbb R),
\tag{14}
\]

and, for some `c_n,R_n>0`,

\[
\boxed{
F_0(\xi)\ge c_n|\xi|^{-1/2}
\qquad(|\xi|\ge R_n).
}
\tag{15}
\]

The exponent is deliberately slower than the finite source-boundary decay in (10). Hence

\[
\frac{|G_f(\xi)|}{F_0(\xi)}
\le
\frac{C_f}{c_n}|\xi|^{-1/2}
\longrightarrow0
\qquad(|\xi|\to\infty).
\tag{16}
\]

On every compact interval, `F_0` has a strictly positive minimum by continuity and (14), while `G_f` is bounded. Therefore

\[
\boxed{
K_f
:=
\sup_{\xi\in\mathbb R}
\frac{|G_f(\xi)|}{F_0(\xi)}
<\infty.
}
\tag{17}
\]

Choose any integer

\[
M>K_f.
\tag{18}
\]

## 3. Direct-sum additivity gives strict Weil-cone positivity

Higher-order Taylor trace remainders are additive under orthogonal direct sums. Therefore the even Fourier multiplier for (3) is exactly

\[
\widetilde F(\xi)
=
M F_0(\xi)+G_f(\xi).
\tag{19}
\]

By (17)--(18),

\[
\widetilde F(\xi)
\ge
M F_0(\xi)-|G_f(\xi)|
>0
\qquad(\xi\in\mathbb R).
\tag{20}
\]

At order `n=4k`, the exact `WP-193` criterion identifies nonnegativity of the Taylor remainder on every real compactly supported smooth autocorrelation with nonnegativity of this even Fourier multiplier. Strict positivity of (20), together with analyticity of the Fourier transform of a nonzero compactly supported `g`, gives (5).

The operator conditions are preserved exactly. Direct sums preserve positivity, and the finite block belongs to every Schatten class, so

\[
\widetilde V\in\mathcal S^n
\tag{21}
\]

because the bath does. Conversely the bath is not in `S^{n-1}`, hence neither is `widetilde V`. If

\[
H_fV_f\ne0,
\tag{22}
\]

then

\[
\widetilde H\widetilde V
=0_{\rm bath}^{\oplus M}\oplus H_fV_f
\ne0.
\tag{23}
\]

Likewise any noncommutativity in the finite block survives unchanged:

\[
[\widetilde H,\widetilde V]
=0_{\rm bath}^{\oplus M}\oplus[H_f,V_f].
\tag{24}
\]

Thus the bath does not repair, simplify, or erase the payload geometry. It only overwhelms its `O(|xi|^{-1})` Fourier sign defect by an independent slower positive tail.

## 4. The theorem applies simultaneously to any finite list of payloads

Let

\[
(H_f^{(1)},V_f^{(1)}),\ldots,
(H_f^{(L)},V_f^{(L)})
\tag{25}
\]

be any finite collection of finite-dimensional positive pairs, and define the constants `K_1,...,K_L` by (17). Choosing

\[
M>\max_{1\le\ell\le L}K_\ell
\tag{26}
\]

makes the same bath multiplicity stabilize every member of the collection separately.

This gives a particularly direct matched control. One payload may encode a finite arithmetic truncation, Prime Circle incidence, Prime Lattice data, or another source-motivated finite geometry, while another may use generic nonarithmetic eigenvalues of the same dimension and norm scale. Both inherit the same full-cone sign after adjoining the bath. The sign therefore cannot distinguish the arithmetic payload from its matched control.

The statement does **not** say that every single fixed bath multiplicity stabilizes an unbounded class of finite payloads. `M` is allowed to depend on the payload or bounded family. That dependence is precisely why this is a falsification control rather than a construction of the desired bridge.

## 5. Aggressive falsification and exact scope

**Could the finite payload alter the bath tail through noncommutativity?** No in this construction. The sectors are orthogonal direct summands, so the trace remainder and spectral-shift density add exactly. Noncommutativity internal to `(H_f,V_f)` remains, but there is no cross-sector interaction capable of changing the bath floor.

**Could a sufficiently complicated finite payload decay more slowly than `1/|xi|` and beat the bath?** Not in the finite matrix category covered by `WP-197`. Equation (7) gives a derivative consisting of an `L^1` part plus finitely many atoms, which forces (9)--(10). Large dimension changes only the constant `C_f`, absorbed into `M`.

**Does the theorem prove that all infinite positive completions are nonselective?** No. It proves a universal stabilization theorem for the specific rough centered reservoir class exposed by `WP-198`, and more generally for any positive reservoir whose Fourier floor dominates `1/|xi|`. A genuinely coupled infinite geometry could evade the direct-sum argument.

**Does the bath produce Gamma, Mangoldt, or polar/global terms?** No. It contains none of them. It is intentionally source-blind. That is the point of the control: if a proposed proof of arithmetic positivity is unchanged after its finite arithmetic sector is replaced by an arbitrary finite positive payload while the bath remains the sign-producing component, the proof has not explained the arithmetic sign.

**Could the reservoir itself be Mathia-native and canonical?** Yes, and this theorem does not rule that out. But canonicality of the reservoir is insufficient if the arithmetic payload merely sits in an orthogonal finite summand whose negative Fourier contribution is dominated externally. A surviving proposal must show a source-forced finite--infinite coupling, quotient, incidence relation, or common global form in which the arithmetic data participate in the sign theorem itself.

**What if the arithmetic sector is already infinite?** The theorem does not classify it. The proof extends to any payload whose even spectral-shift multiplier `G` is continuous and satisfies

\[
G(\xi)=o(|\xi|^{-1/2})
\tag{27}
\]

relative to the bath lower bound, provided direct-sum additivity and the relevant trace formula remain valid. The finite-dimensional theorem is the clean source-independent case guaranteed by `WP-197`.

## 6. Prior art and novelty boundary

The ingredients are classical operator/Fourier theory plus the branch-specific controls already isolated in `WP-193`, `WP-197`, and `WP-198`.

Higher-order spectral-shift functions and trace formulas under Schatten perturbations are standard; a principal reference used by this line is Denis Potapov, Anna Skripka, and Fedor Sukochev, *Spectral shift function of higher order*, Inventiones Mathematicae **193** (2013), 501--538, DOI `10.1007/s00222-012-0431-2`. Finite-matrix source-jump structure used in `WP-197` comes from the corresponding multiple-operator-integral/spectral-shift literature. Direct-sum additivity of traces, Riemann--Lebesgue decay, and domination of an `O(|xi|^{-1})` multiplier by a positive `|xi|^{-1/2}` floor are elementary once the two exact asymptotics are known.

A targeted literature search for higher-order spectral-shift Fourier positive-definiteness and Schatten perturbations found the established trace/integrability theory, including modern all-order spectral-shift work, but no theorem phrased as the `WP-199` universal stabilization statement. Absence of a wording match is not treated as standalone novelty. The durable new content for Mathia is the exact synthesis of the two already-established branch boundaries: `WP-197` supplies the universal finite `1/xi` defect, while `WP-198` supplies a source-blind slower positive floor. Together they show that **every** finite monotone-positive payload can be hidden inside full `4k` Weil-cone positivity once the rough bath category is admitted.

This is not a candidate proof of Weil positivity and should not be confused with classical Weil, Hilbert--Pólya, Connes trace, Sonin/localization, Frobenius/cohomological, or intersection-form approaches. It is an adversarial matched control on what an independent geometric sign theorem would have to explain.

## 7. Consequence for `weil_positivity`

The infinite-dimensional escape of `WP-198` is more nonselective than its one-channel example suggests. In the natural `S^{4k}` class, a generic rough centered reservoir can act as a positivity stabilizer around any finite positive geometry. Consequently the research line should reject the architecture

\[
\text{finite arithmetic payload}
\quad\oplus\quad
\text{independent rough sign-producing bath}
\tag{28}
\]

as explanatory evidence, even when the completed object is perfectly positive on the full Weil autocorrelation cone.

The live requirement is stronger: the critical infinite reservoir must be **source-forced and nonseparably coupled** to the finite-prime, Gamma, and polar/global sectors before positivity is taken. The arithmetic structure must constrain the sign-producing geometry, rather than merely survive as a finite perturbation that an unrelated universal bath can dominate.

This supplies a practical matched-control test for future infinite-dimensional candidates. Replace the candidate's finite arithmetic sector by an arbitrary finite positive pair while leaving the claimed reservoir and sign mechanism unchanged. If a finite amplification of the same reservoir still proves full-cone positivity, the mechanism is generic stabilization rather than arithmetic explanation.

## Dependencies

- `research/weil_positivity/findings/WP-193-higher-order-spectral-shift-positivity-has-a-mod-four-weil-autocorrelation-gate.md`
- `research/weil_positivity/findings/WP-197-noncommuting-monotone-positive-finite-backgrounds-still-force-zero-mode-support-at-order-4k.md`
- `research/weil_positivity/findings/WP-198-rough-infinite-centered-bath-defeats-finite-positive-source-4k-no-go.md`

## Bottom line

For every finite-dimensional monotone-positive pair `(H_f,V_f)` and every order `n=4k`, the `WP-198` centered bath can be repeated finitely many times so that its `|xi|^{-1/2}` positive Fourier floor dominates the payload's universal `O(|xi|^{-1})` sign defect. The direct sum remains a monotone-positive pair in `S^{4k}\setminus S^{4k-1}` and is strictly positive on the entire Weil autocorrelation cone, while preserving any nonzero `H_fV_f` and any noncommutativity inside the finite block.

Thus rough infinite `4k` cone positivity is **finitely universal rather than arithmetically selective**. Any Mathia-native use of this category must derive a nonseparable arithmetic coupling to the reservoir; appending an independent rough bath to a finite arithmetic sector cannot count as the sought geometric Weil positivity mechanism.