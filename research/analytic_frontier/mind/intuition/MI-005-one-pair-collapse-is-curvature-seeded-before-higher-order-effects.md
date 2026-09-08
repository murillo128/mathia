# MI-005 — Fixed-notch success is controlled by non-excisable mesoscopic source exposure and its forced companion

**Evidence level:** supported by exact fixed-notch reduction, full-profile Gaussian comparison, and global-completion constraints through ANF-120

## Core intuition

The frozen-notch problem is not controlled by raw Gram conditioning, maximal packet height, componentwise source mass, or finitely many saddle phases. The exact obstruction lives at the `A^(-1/2)` interior-saddle scale and must be evaluated **after the packet is embedded into a global near-extremizer**.

ANF-118 removes the need to approximate that scale by a finite jet: throughout its subexponential cloud envelope, one explicit Gaussian Gram form measures the complete same-saddle source profile. ANF-119--ANF-120 then show that a source-heavy off-notch profile cannot be completed arbitrarily. Near-extremality forces either excision, extra same-band polarization, or asymptotic profile mirroring; near maximal notch efficiency forces mirroring even in the bounded-mass branch.

The surviving question is therefore whether the source permits a globally non-excisable **profile-plus-companion architecture** that cancels strongly off the notch while still generating the separate central-notch exposure required by a fatal near-extremizer.

## Strongest justified principle

ANF-115 constructs distinct physical packets with `O(A)` horizontal span whose source spectrum concentrates at a stable interior saddle `|alpha|=a_gamma<1`, whose normalized capacity deficit remains linear in `A`, and which can remain invisible to a fixed central notch. ANF-116 shows that finitely many translates can phase-balance inside a genuine global near-extremizer and become excisable as an aggregate. ANF-117 proves that every fixed finite saddle jet can vanish while order-one source mass survives at the natural mesoscopic width.

ANF-118 replaces all finite-jet bookkeeping by the full positive Gaussian Gram form. For positive translation clouds with `log(e+V_A)=o(A^(1/3))`, normalized source mass equals that Gram mass up to `o(1)` relative/additive error. Thus vanishing of the full mesoscopic profile, rather than vanishing of any finite list of derivatives, is the correct internal excision criterion in that envelope.

ANF-119 supplies the external completion trichotomy. A source-negligible packet is removable; a bounded source-heavy packet is removable when the complement remains near-extremal and otherwise forces an overpolarized same-band companion; a diverging packet forces the complement to reproduce its localized profile with opposite phase. ANF-120 adds the fixed-notch efficiency constraint: for bounded packet mass, the off-notch remainder satisfies a two-sided mismatch corridor, and `h_eta/chi_eta -> 1` forces the packet and complement to mirror asymptotically in the saddle band.

## Counterevidence / boundary

None of ANF-118--ANF-120 constructs a fatal near-extremizer or proves `beta_eta<B_eta`. The ANF-118 comparison has a real scale boundary: exponentially large cloud weight can move the physical saddle and escape the fixed-saddle Gaussian proxy. ANF-120's strongest bounded-mass mirroring conclusion is conditional on approach to maximal notch efficiency; it is not a theorem that every bounded near-extremal completion mirrors.

The remaining architecture may also use source geometry outside the same-saddle positive-translation class. Such a category exit is not evidence by itself; it must still satisfy the exact global near-extremal and notch budgets.

## Epistemic status

**Exact full-profile control and exact global-completion constraints; exclusion or construction of the final coupled non-excisable profile-plus-companion remains open.**

## Falsification criterion

Construct a physical global near-extremizer in which a non-excisable interior-saddle aggregate survives the ANF-118 full-profile test, satisfies the ANF-119/ANF-120 companion constraints, and reaches the fatal fixed-notch exposure. Conversely, prove that every such globally admissible profile-plus-companion configuration is excisable or loses enough central-notch exposure to force `beta_eta<B_eta`. A proof depending only on componentwise mass or finitely many saddle derivatives is already falsified by ANF-116--ANF-118.